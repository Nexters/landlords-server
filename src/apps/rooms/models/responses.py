from typing import List

from pydantic import BaseModel, Field

from .entity import Address, Description, Uid


class RoomItemResponse(BaseModel):
    uid: str = Field(max_length=Uid.max_length)
    deposit: int = Field(...)
    monthly_rent: int = Field(...)
    is_jeonse: bool = Field(...)
    address: str = Field(max_length=Address.max_length)
    description: str = Field(max_length=Description.max_length)

    class Config:
        orm_mode = True


class RoomItemsResponse(BaseModel):
    rooms: List[RoomItemResponse]
