from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic.dataclasses import dataclass

from ..entity import BuildingType, SellingType
from .landlords import RoomItem

image_url = "https://ic.zigbang.com/ic/items/{uid}/1.jpg?w={width}&h={height}"


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


class ZigbangSellingType(str, Enum):
    MonthlyRent = "월세"
    Jeonse = "전세"
    Selling = "매매"


mapper = {
    ZigbangBuildingType.Apartment: BuildingType.Apartment,
    ZigbangBuildingType.OneRoom: BuildingType.OneRoom,
    ZigbangBuildingType.Officetel: BuildingType.Officetel,
    ZigbangBuildingType.Villa: BuildingType.Villa,
    ZigbangSellingType.MonthlyRent: SellingType.MonthlyRent,
    ZigbangSellingType.Jeonse: SellingType.Jeonse,
    ZigbangSellingType.Selling: SellingType.Selling
}


@dataclass
class Zigbang:
    items: List[Item]

    def to_room(self) -> RoomItem:
        item = self.items.pop()
        zigbang_selling_type = ZigbangSellingType(item.sales_type)
        zigbang_building_type = ZigbangBuildingType(item.service_type)

        return RoomItem(
            uid=f"Zigbang::{item.item_id}",
            deposit=item.deposit,
            monthly_rent=item.rent,
            selling_type=SellingType(mapper[zigbang_selling_type]),
            address=item.address,
            title=item.title,
            description=item.description,
            image=image_url.format(uid=item.item_id, width=800, height=600),
            building_type=BuildingType(mapper[zigbang_building_type]),
        )
