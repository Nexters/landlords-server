from typing import List

from fastapi import status
from fastapi.param_functions import Depends, Path
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from ...core.database import get_database_session
from .exceptions import RoomNotFoundException
from .models.entity import Room
from .models.requests import RoomItemCreateRequest, RoomItemUpdateRequest
from .models.responses import RoomItemResponse, RoomItemsResponse

router = APIRouter()
__valid_uid = Path(..., min_length=1)


@router.get(
    path="/{uid}",
    name="방 매물 정보 불러오기",
    status_code=status.HTTP_200_OK,
    response_model=RoomItemResponse,
)
async def get_room(
    uid: str = __valid_uid, session: Session = Depends(get_database_session)
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
    session: Session = Depends(get_database_session)
) -> RoomItemsResponse:
    rooms_orm: List[Room] = session.query(Room).all()
    if not rooms_orm:
        raise RoomNotFoundException("등록된 방 매물이 없습니다")
    return RoomItemsResponse(
        rooms=[RoomItemResponse.from_orm(room) for room in rooms_orm]
    )


@router.post(
    path="",
    name="방 매물 정보 등록",
    status_code=status.HTTP_201_CREATED,
    response_model=RoomItemResponse,
)
async def post_room(
    request: RoomItemCreateRequest,
    session: Session = Depends(get_database_session),
) -> RoomItemResponse:
    room_orm = Room(**request.dict())
    session.add(room_orm)
    session.commit()
    session.refresh(room_orm)
    return RoomItemResponse.from_orm(room_orm)


@router.patch(
    path="/{uid}",
    name="방 매물 정보 업데이트",
    status_code=status.HTTP_200_OK,
    response_model=RoomItemResponse,
)
async def update_room(
    update_request: RoomItemUpdateRequest,
    uid: str = __valid_uid,
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
    uid: str = __valid_uid, session: Session = Depends(get_database_session)
) -> None:
    room = session.query(Room).filter(Room.uid == uid).first()
    if not room:
        raise RoomNotFoundException(f"{uid}에 해당하는 방 매물이 없습니다")
    session.delete(room)
    session.commit()
