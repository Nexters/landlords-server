from typing import List

from pydantic import BaseModel

from .domain import RoomItem


class RoomItemResponse(RoomItem):
    """ 방 매물 정보 response """


class RoomItemsResponse(BaseModel):
    """ 방 매물 정보 리스트 response """

    rooms: List[RoomItem]
