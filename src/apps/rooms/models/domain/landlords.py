from enum import Enum, IntEnum
from typing import Optional

from pydantic import BaseModel, Field


class Description(IntEnum):
    max_length = 3000


class Uid(IntEnum):
    max_length = 100


class Address(IntEnum):
    max_length = 100


class Title(IntEnum):
    max_length = 100


class Image(IntEnum):
    max_length = 300


class Floor(IntEnum):
    max_length = 20


class AdministrativeExpenses(IntEnum):
    max_length = 20


class RoomSize(IntEnum):
    max_precision = 7
    max_scale = 2


class CrawlingTarget(str, Enum):
    """ 크롤링 대상 """

    Dabang = "Dabang"
    Zigbang = "Zigbang"


class BuildingType(str, Enum):
    OneRoom = "OneRoom"
    TwoRoom = "TwoRoom"
    ThreeRoom = "ThreeRoom"
    Officetel = "Officetel"
    Apartment = "Apartment"
    Villa = "Villa"


class SellingType(str, Enum):
    MonthlyRent = "MonthlyRent"  # 월세
    Jeonse = "Jeonse"  # 전세
    Selling = "Selling"  # 매매


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
    room_size: float = Field(
        maximum=(10 ** (RoomSize.max_precision - RoomSize.max_scale)) - 1,
        description="방 크기(㎡)",
    )
    floor: str = Field(max_length=Floor.max_length, description="층/건물층수")
    has_elevator: Optional[bool] = Field(default=None, description="엘리베이터 유무")
    administrative_expenses: int = Field(
        maximum=(10 ** AdministrativeExpenses.max_length) - 1, description="관리비"
    )

    class Config:
        orm_mode = True


class RoomItemInDB(RoomItem):
    user_id: int = Field(...)
