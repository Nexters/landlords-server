from typing import List, Union

from fastapi import BackgroundTasks, status
from fastapi.logger import logger
from fastapi.param_functions import Depends, Path, Security
from fastapi.routing import APIRouter
from sqlalchemy import and_
from sqlalchemy.orm import Session

from ...core.database import get_database_session
from ...core.exceptions import CrawlingException
from ..checklist.models.domain import CheckAnswer as CheckAnswerDto
from ..checklist.models.domain import CheckItem as CheckItemDto
from ..checklist.models.entity import CheckAnswer
from ..oauth.entity import User
from ..oauth.models import UserInDB
from ..oauth.services import get_current_user
from .exceptions import RoomNotFoundException
from .models.domain.dabang import Dabang
from .models.domain.landlords import CrawlingTarget
from .models.domain.zigbang import Zigbang
from .models.entity import Room
from .models.requests import RoomItemCreateRequest, RoomItemUpdateRequest
from .models.responses import RoomItemResponse, RoomItemsResponse
from .services import get_room_detail

router = APIRouter()
__valid_uid = Path(..., min_length=1, description="고유 ID")


@router.get(
    path="/{uid}",
    name="방 매물 정보 불러오기",
    status_code=status.HTTP_200_OK,
    response_model=RoomItemResponse,
)
async def get_room(
    uid: str = __valid_uid,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> RoomItemResponse:
    room_orm = session.query(Room).filter(Room.uid == uid).first()
    if not room_orm:
        raise RoomNotFoundException("등록된 방이 아닙니다")
    return RoomItemResponse.from_orm(room_orm)


@router.get(
    path="",
    name="방 매물 리스트 불러오기",
    status_code=status.HTTP_200_OK,
    response_model=RoomItemsResponse,
)
async def get_rooms(
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> RoomItemsResponse:
    rooms_orm: List[Room] = session.query(Room).all()
    if not rooms_orm:
        raise RoomNotFoundException("등록된 방 매물이 없습니다")
    return RoomItemsResponse(
        rooms=[RoomItemResponse.from_orm(room) for room in rooms_orm]
    )


@router.get(
    path="/{room_id}/answers",
    name="체크리스트 응답리스트 불러오기",
    status_code=status.HTTP_200_OK,
    response_model=List[CheckItemDto],
)
async def get_checklist_answers(
    room_id: str = __valid_uid,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> List[CheckItemDto]:
    answers = (
        session.query(CheckAnswer)
        .filter_by(user_id=current_user.uid)
        .join(User, User.uid == CheckAnswer.user_id)
        .join(Room, Room.uid == room_id)
        .all()
    )

    return [CheckAnswerDto.from_orm(answer).check for answer in answers]


@router.post(
    path="",
    name="방 매물 정보 등록",
    status_code=status.HTTP_201_CREATED,
    response_model=RoomItemResponse,
)
async def post_room(
    request: RoomItemCreateRequest,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> RoomItemResponse:
    room_orm = Room(**request.dict())
    session.add(room_orm)
    session.commit()
    session.refresh(room_orm)
    return RoomItemResponse.from_orm(room_orm)


@router.post(
    path="/{room_id}/answers",
    name="체크리스트 응답 저장",
    status_code=status.HTTP_201_CREATED,
    response_model=CheckItemDto,
)
async def post_checklist_answer(
    room_id: str = __valid_uid,
    check_id: int = 0,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> CheckItemDto:

    answer = CheckAnswer(
        user_id=current_user.uid, room_id=room_id, check_id=check_id
    )

    session.add(answer)
    session.commit()
    session.refresh(answer)
    return CheckItemDto.from_orm(answer.check)


@router.patch(
    path="/{uid}",
    name="방 매물 정보 업데이트",
    status_code=status.HTTP_200_OK,
    response_model=RoomItemResponse,
)
async def update_room(
    update_request: RoomItemUpdateRequest,
    uid: str = __valid_uid,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> RoomItemResponse:
    room = session.query(Room).filter(Room.uid == uid).first()
    if not room:
        raise RoomNotFoundException(f"{uid}에 해당하는 방 매물이 없습니다")
    old_room = RoomItemResponse.from_orm(room)
    update_data = update_request.dict()
    for field, value in old_room:
        if field in update_data:
            setattr(room, field, update_data[field])
    session.add(room)
    session.commit()

    return RoomItemResponse.from_orm(room)


@router.delete(
    path="/{uid}", name="방 매물 정보 삭제", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_room(
    uid: str = __valid_uid,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> None:
    room = session.query(Room).filter(Room.uid == uid).first()
    if not room:
        raise RoomNotFoundException(f"{uid}에 해당하는 방 매물이 없습니다")
    session.delete(room)
    session.commit()


@router.delete(
    path="/{room_id}/answers",
    name="체크리스트 응답 삭제",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_checklist_answer(
    room_id: str = __valid_uid,
    check_id: int = 0,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> None:
    checkAnswer = (
        session.query(CheckAnswer)
        .filter(
            and_(
                CheckAnswer.check_id == check_id,
                User.uid == current_user.uid,
                CheckAnswer.room_id == room_id,
            )
        )
        .first()
    )

    session.delete(checkAnswer)
    session.commit()


@router.put(
    path="/{room_id}",
    name="방 매물 정보 크롤링",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def crawling_room(
    background_tasks: BackgroundTasks,
    room_id: str = __valid_uid,
    crawling_target: CrawlingTarget = CrawlingTarget.Dabang,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> None:
    """ 추후 websocket으로 결과 notification """
    room = (
        session.query(Room)
        .filter(Room.uid == f"{crawling_target.value}::{room_id}")
        .first()
    )
    if not room:
        background_tasks.add_task(
            __crawling_room,
            room_id=room_id,
            crawling_target=crawling_target,
            session=session,
        )


def __crawling_room(
    room_id: str, crawling_target: CrawlingTarget, session: Session
) -> None:
    uid = f"{crawling_target.value}::{room_id}"
    try:
        bang: Union[Zigbang, Dabang] = get_room_detail(
            room_id=room_id, crawling_target=crawling_target
        )
    except CrawlingException as err:
        logger.error(f"{type(err).__name__}: {err}")
    else:
        room = bang.to_room()
        room_orm = Room(**room.dict())
        session.add(room_orm)
        session.commit()
