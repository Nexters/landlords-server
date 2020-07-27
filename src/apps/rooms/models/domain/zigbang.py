from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic.dataclasses import dataclass

from ..entity import BuildingType
from .landlords import RoomItem


@dataclass
class RoomTypeTitle:
    p: Optional[int] = None
    m2: Optional[int] = None


@dataclass
class Area:
    p: Optional[float] = None
    m2: Optional[float] = None


@dataclass
class Item:
    size_m2: Optional[int] = None
    building_floor: Optional[int] = None
    section_type: Optional[str] = None
    item_id: Optional[int] = None
    images_thumbnail: Optional[str] = None
    sales_type: Optional[str] = None
    sales_title: Optional[str] = None
    deposit: int = 0
    rent: int = 0
    공급면적: Optional[Area] = None
    전용면적: Optional[Area] = None
    계약면적: Optional[Area] = None
    room_type_title: Optional[RoomTypeTitle] = None
    floor: Optional[str] = None
    floor_string: Optional[str] = None
    title: Optional[str] = None
    address: Optional[str] = None
    is_zzim: Optional[bool] = None
    status: Optional[bool] = None
    service_type: Optional[str] = None
    tags: Optional[List[str]] = None
    is_first_movein: Optional[Any] = None
    room_type: Optional[int] = None
    random_location: Optional[Any] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    address3: Optional[str] = None
    manage_cost: Optional[Any] = None
    reg_date: Optional[datetime] = None
    is_new: Optional[bool] = None
    description: Optional[str] = None


class ZigbangBuildingType(str, Enum):
    Apartment = "아파트"
    OneRoom = "원룸"
    Officetel = "오피스텔"
    Villa = "빌라"


mapper = {
    ZigbangBuildingType.Apartment: BuildingType.Apartment,
    ZigbangBuildingType.OneRoom: BuildingType.OneRoom,
    ZigbangBuildingType.Officetel: BuildingType.Officetel,
    ZigbangBuildingType.Villa: BuildingType.Villa,
}


@dataclass
class Zigbang:
    items: List[Item]

    def to_room(self) -> RoomItem:
        item = self.items.pop()

        return RoomItem(
            uid=f"Zigbang::{item.item_id}",
            deposit=item.deposit,
            monthly_rent=item.rent,
            is_jeonse=(item.sales_type == "전세"),
            address=item.address,
            title=item.title,
            description=item.description,
            building_type=mapper[ZigbangBuildingType(item.service_type)],
        )
