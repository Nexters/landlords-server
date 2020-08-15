from typing import List, Union

from fastapi import Response, status
from fastapi.logger import logger
from fastapi.param_functions import Depends, Path, Security
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from ...core.database import get_database_session
from ...core.exceptions import CrawlingException
from ..checklist.models.domain import CheckItem as CheckItemDto
from ..checklist.models.entity import CheckAnswer, CheckItem
from ..checklist.models.requests import AnswerCreateRequest
from ..checklist.models.responses import CheckItemResponse, CheckItemsResponse
from ..oauth.models.domain.landlords import UserInDB
from ..oauth.models.entity import User
from ..oauth.services import get_current_user
from .exceptions import AnswerNotFoundException, RoomNotFoundException
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
    room_orm = (
        session.query(Room)
        .filter((Room.uid == uid) & (Room.user_id == current_user.uid))
        .first()
    )
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
    rooms_orm: List[Room] = session.query(Room).filter(
        Room.user_id == current_user.uid
    ).all()
    if not rooms_orm:
        raise RoomNotFoundException("등록된 방 매물이 없습니다")
    return RoomItemsResponse(
        rooms=[RoomItemResponse.from_orm(room) for room in rooms_orm]
    )


@router.get(
    path="/{room_id}/answers",
    name="체크리스트 응답리스트 불러오기",
    status_code=status.HTTP_200_OK,
    response_model=CheckItemsResponse,
)
async def get_checklist_answers(
    room_id: str = __valid_uid,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> CheckItemsResponse:
    results = (
        session.query(CheckAnswer, CheckItem)
        .filter(
            (CheckAnswer.user_id == current_user.uid)
            & (CheckAnswer.room_id == room_id)
        )
        .join(CheckItem, CheckItem.uid == CheckAnswer.check_id)
        .all()
    )

    if not results:
        raise AnswerNotFoundException("체크리스트에 응답한 목록이 없습니다.")

    return CheckItemsResponse(
        check_items=[
            CheckItemDto.from_orm(check_item) for _, check_item in results
        ]
    )


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
    room_orm = Room(user_id=current_user.uid, **request.dict())
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
    request: AnswerCreateRequest,
    room_id: str = __valid_uid,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> CheckItemResponse:

    answer_orm = CheckAnswer(
        user_id=current_user.uid, room_id=room_id, check_id=request.check_id
    )

    session.add(answer_orm)
    session.commit()
    session.refresh(answer_orm)
    return CheckItemResponse.from_orm(answer_orm.check)


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
    room = (
        session.query(Room)
        .filter((Room.uid == uid) & (Room.user_id == current_user.uid))
        .first()
    )
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
    room = (
        session.query(Room)
        .filter((Room.uid == uid) & (Room.user_id == current_user.uid))
        .first()
    )
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
    check_id: int,
    room_id: str = __valid_uid,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> None:
    answer_orm = (
        session.query(CheckAnswer)
        .filter(
            (CheckAnswer.check_id == check_id)
            & (User.uid == current_user.uid)
            & (CheckAnswer.room_id == room_id)
        )
        .first()
    )

    if not answer_orm:
        raise AnswerNotFoundException("체크되지 않은 응답입니다.")

    session.delete(answer_orm)
    session.commit()


@router.put(
    path="/{room_id}",
    name="방 매물 정보 크롤링",
    responses={
        "200": {"model": RoomItemResponse},
        "201": {"model": RoomItemResponse},
    },
)
async def crawling_room(
    response: Response,
    room_id: str = __valid_uid,
    crawling_target: CrawlingTarget = CrawlingTarget.Dabang,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> RoomItemResponse:

    room = (
        session.query(Room)
        .filter(
            (Room.uid == f"{crawling_target.value}::{room_id}")
            & (Room.user_id == current_user.uid)
        )
        .first()
    )

    if not room:
        room = __crawling_room(
            room_id=room_id,
            user_id=current_user.uid,
            crawling_target=crawling_target,
            session=session,
        )
        response.status_code = status.HTTP_201_CREATED
    else:
        response.status_code = status.HTTP_200_OK

    return RoomItemResponse.from_orm(room)


def __crawling_room(
    room_id: str,
    user_id: int,
    crawling_target: CrawlingTarget,
    session: Session,
) -> Room:
    try:
        bang: Union[Zigbang, Dabang] = get_room_detail(
            room_id=room_id, crawling_target=crawling_target
        )
    except CrawlingException as err:
        logger.error(f"{type(err).__name__}: {err}")
    else:
        room = bang.to_room()
        room_orm = Room(user_id=user_id, **room.dict())
        session.add(room_orm)
        session.commit()

    return room_orm
