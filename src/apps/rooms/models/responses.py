from typing import List

from pydantic import BaseModel

from .domain.landlords import RoomItemInDB


class RoomItemResponse(RoomItemInDB):
    """ 방 매물 정보 response """


class RoomItemsResponse(BaseModel):
    """ 방 매물 정보 리스트 response """

    rooms: List[RoomItemInDB]
