from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from ..entity import (
    Address,
    BuildingType,
    Description,
    Image,
    SellingType,
    Title,
    Uid,
)


class CrawlingTarget(str, Enum):
    """ 크롤링 대상 """

    Dabang = "Dabang"
    Zigbang = "Zigbang"


class RoomItem(BaseModel):
    uid: str = Field(max_length=Uid.max_length)
    deposit: int = Field(...)
    monthly_rent: int = Field(...)
    selling_type: SellingType = Field(...)
    address: Optional[str] = Field(max_length=Address.max_length)
    title: Optional[str] = Field(max_length=Title.max_length)
    description: Optional[str] = Field(max_length=Description.max_length)
    image: Optional[str] = Field(max_length=Image.max_length)
    building_type: BuildingType = Field(...)

    class Config:
        orm_mode = True


class RoomItemInDB(RoomItem):
    user_id: int = Field(...)
