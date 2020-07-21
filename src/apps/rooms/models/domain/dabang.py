from datetime import datetime
from enum import IntEnum
from typing import Any, List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..entity import BuildingType
from .landlords import RoomItem


class SellingType(IntEnum):
    MonthlyRent = 0  # 월세
    Jeonse = 1  # 전세
    Selling = 2  # 매매


@dataclass
class Agent:
    id: Optional[str]
    email: Optional[str]
    name: Optional[str]
    facename: Optional[str]
    address: Optional[str]
    location: Any
    reg_id: Optional[str]
    business_id: Optional[str]
    saved_time: datetime
    active: bool
    is_primary: bool
    user_name: Optional[str]
    user_phone: Optional[str]
    user_safe_phone: Optional[str]
    user_tel: Optional[str]
    users_idx: int
    sub_emails: Any
    is_premium: bool
    review_best_count: int
    review_count: int
    is_messenger_actived: bool
    profile_url: Optional[str]
    message: Optional[str]
    since: Optional[str]
    is_awards: bool
    emails: List[str]
    role_type: Optional[str]


@dataclass
class Image:
    image: Optional[str]
    image_title: Optional[str]
    image_desc: Any
    location: List[float]


@dataclass
class Complex:
    complex_id: Optional[str]
    complex_type: int
    complex_name: Optional[str]
    household_num: int
    building_num: int
    parking_num: int
    manage_tel: Optional[str]
    complex_lowest_floor: int
    complex_highest_floor: int
    build_cov_ratio: int
    floor_area_index: int
    provider_name: Optional[str]
    address: Optional[str]
    jibun_address: Optional[str]
    road_address: Optional[str]
    location: List[float]
    parking_average: float
    is_favorited: Any
    favorited_count: int
    is_default_image: bool
    complex_type_str: Optional[str]
    parking_type_str: Any
    heat_type_str: Optional[str]
    fuel_type_str: Optional[str]
    enter_date_str: Optional[str]
    represent_image: Optional[str]
    entrance_type_str: Any
    real_price_max_trade: Any
    real_price_min_trade: Any
    real_price_max_lease: Any
    real_price_min_lease: Any
    maintenance_standard: Optional[str]
    maintenance_last_price: Any
    maintenance_total_price: Any
    maintenance_summer_total_price: Any
    maintenance_winter_total_price: Any
    trade_region_average_pyeong_price: Any
    lease_region_average_pyeong_price: Any
    trade_average_pyeong_price: Any
    lease_average_pyeong_price: Any
    images: List[Image]


@dataclass
class Contact:
    call_number: Optional[str]
    sms_message: Optional[str]
    show_number: Optional[str]
    sms_number: Optional[str]


@dataclass
class DetailShop:
    use: bool
    link: Optional[str]


@dataclass
class OtherRoom:
    is_favorited: Any
    seq: int
    id: Optional[str]
    user_id: Optional[str]
    status: int
    deleted: bool
    name: Optional[str]
    title: Optional[str]
    room_type: int
    location: List[float]
    random_location: List[float]
    premium_badge: Any
    hash_tags: List[str]
    room_type_str: Optional[str]
    room_desc: Optional[str]
    img_url: Optional[str]
    img_urls: List[str]
    is_pano: bool
    price_title: Optional[str]
    selling_type: SellingType
    is_confirm: bool
    confirm_type: Any
    confirm_date_str: Optional[str]
    is_quick: bool
    is_messenger_actived: bool
    complex_name: Optional[str] = None


@dataclass
class ReviewElement:
    id: int
    room_id: Any
    agent_id: Optional[str]
    review_text: Optional[str]
    user_id: Optional[str]
    grade: int
    has_comment: bool
    agent_name: Optional[str]
    comment_user_id: Optional[str]
    comment_text: Optional[str]
    comment_position: Optional[str]
    comment_user_name: Optional[str]
    comment_is_primary: Optional[bool]
    comment_role_type: Optional[int]
    saved_time: Optional[datetime]
    edited_time: Optional[datetime]
    comment_saved_time: Optional[datetime]
    seq: Any
    user_active: bool
    agent_profile_url: Optional[str]
    user_profile_url: Optional[str]


@dataclass
class DabangReview:
    review_count_good: int
    reviews: List[ReviewElement]
    review_count: int


@dataclass
class DeungbonSummary:
    detailScore: Optional[str] = Field(
        ..., title="detail_score", alias="detailScore"
    )  # noqa
    regCommentTagMapList: Optional[List[Any]] = Field(
        ..., title="reg_comment_tag_map_list", alias="regCommentTagMapList"
    )  # noqa
    grade: int = Field(...)
    grade_message: Optional[str] = Field(...)
    report_url: Any = Field(...)
    report_date: Optional[str] = Field(...)


@dataclass
class Photo:
    key: Optional[str]
    desc: Optional[str]


@dataclass
class RoomOption:
    seq: int
    name: Optional[str]


@dataclass
class Room:
    is_favorited: Any
    favorited_count: int
    seq: int
    id: Optional[str]
    user_id: Optional[str]
    status: int
    title: Optional[str]
    memo: Optional[str]
    private_memo: Any
    room_type: int
    maintenance_option: int
    room_size: float
    provision_size: Any
    pano: Any
    moving_date: Optional[str]
    card: bool
    photos: List[str]
    photo: List[Photo]
    price_info: List[List[int]]
    address: Optional[str]
    location: List[float]
    random_location: List[float]
    shorten_url: Optional[str]
    agent_id: Optional[str]
    division: bool
    duplex: bool
    full_option: bool
    complex_id: Optional[str]
    dong: Optional[str]
    ho: Optional[str]
    contract_size: Optional[float]
    enter_date: Optional[int]
    room_type_str: Optional[str]
    room_type_main_str: Optional[str]
    maintenance_items_str: List[str]
    heating: Optional[str]
    room_floor_str: Optional[str]
    building_floor_str: Optional[str]
    maintenance_cost_str: Optional[str]
    full_options: List[str]
    etc_options: List[str]
    price_hash_tags: List[str]
    option_hash_tags: List[str]
    detail_hash_tags: List[str]
    hash_tags: List[str]
    price_title: Optional[str]
    price_info_str: List[List[str]]
    animal_str: Optional[str]
    parking_str: Optional[str]
    elevator_str: Optional[str]
    loan_str: Optional[str]
    built_in_str: Optional[str]
    balcony_str: Optional[str]
    duplex_str: Optional[str]
    division_str: Any
    short_lease_str: Optional[str]
    is_show: bool
    is_show_new: bool
    is_confirm: bool
    confirm_type: Any
    confirm_date_str: Optional[str]
    is_quick: Any
    selling_type: SellingType
    month_total_str: Optional[str]
    month_total_cost_str: Optional[str]
    building_use: Any
    deungbon_summary: Optional[DeungbonSummary]
    beds_num: int
    bath_num: int
    show_watermark: bool
    room_options: List[RoomOption]
    safeties: List[RoomOption]


@dataclass
class Average:
    price: float
    options: int
    near: int
    maintenance: int
    traffic: int


@dataclass
class Score:
    average: Average
    total: float
    message: Optional[str]
    room: Average


@dataclass
class Shinhanbank:
    deposit: int
    location: int


@dataclass
class Space:
    space_seq: int
    pyeong_type: Optional[str]
    pyeong: int
    household_num: int
    beds_num: int
    bath_num: int
    exclusive_space: float
    supply_space: Any
    contract_space: float
    entrance_type_str: Optional[str]
    real_price_max_trade: Any
    real_price_min_trade: Any
    real_price_max_lease: Any
    real_price_min_lease: Any
    has_trade_real_price: bool
    has_lease_real_price: bool
    maintenance_last_price: Any
    maintenance_total_price: Any
    maintenance_summer_total_price: Any
    maintenance_winter_total_price: Any
    maintenance_total_price_str: Optional[str]
    layout_image: Optional[str]
    extend_layout_image: Any


@dataclass
class User:
    idx: int
    email: Optional[str]
    name: Optional[str]
    active: bool
    inquery_phone: Optional[str]
    phone: Optional[str]
    tel: Optional[str]
    safe_phone: Optional[str]
    yellow_id: Any
    is_subscribe: bool
    position: Any
    profile_url: Optional[str]
    message: Optional[str]
    role_type: Optional[str]


@dataclass
class Dabang:
    is_messenger_sender_agented: bool
    ios_score_height: int
    agent: Agent
    detail_shop: DetailShop
    bubble_image: Any
    room: Room
    is_messenger_actived: bool
    score: Score
    review: DabangReview
    is_messenger_receipted: bool
    contact: Contact
    other_rooms: List[OtherRoom]
    shinhanbank: Shinhanbank
    messenger_send_alimtalk_contents: Optional[str]
    user: User
    messenger_bubble_contents: Optional[str]
    complex: Optional[Complex] = None
    space: Optional[Space] = None

    def to_room(self) -> RoomItem:
        deposit, monthly_rent, _ = self.room.price_info.pop()
        return RoomItem(
            uid=f"Dabang::{self.room.id}",
            deposit=deposit,
            monthly_rent=monthly_rent,
            is_jeonse=(self.room.selling_type == SellingType.Jeonse),
            address=self.room.address,
            title=self.room.title,
            description=self.room.memo,
            building_type=BuildingType(self.room.room_type),
        )
