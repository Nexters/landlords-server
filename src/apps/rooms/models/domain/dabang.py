from datetime import datetime
from typing import Any, List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ...exceptions import NoneTypeError
from ..entity import BuildingType, SellingType
from .landlords import RoomItem

image_url = "http://d1774jszgerdmk.cloudfront.net/512/{image_key}"


@dataclass
class Agent:
    id: Optional[str]
    email: Optional[str]
    name: Optional[str]
    facename: Optional[str]
    address: Optional[str]
    location: Optional[Any]
    reg_id: Optional[str]
    business_id: Optional[str]
    saved_time: Optional[datetime]
    active: Optional[bool]
    is_primary: Optional[bool]
    user_name: Optional[str]
    user_phone: Optional[str]
    user_safe_phone: Optional[str]
    user_tel: Optional[str]
    users_idx: Optional[int]
    sub_emails: Optional[Any]
    is_premium: Optional[bool]
    review_best_count: Optional[int]
    review_count: Optional[int]
    is_messenger_actived: Optional[bool]
    profile_url: Optional[str]
    message: Optional[str]
    since: Optional[str]
    is_awards: Optional[bool]
    emails: Optional[List[str]]
    role_type: Optional[str]
    agent_tel: Optional[str]


@dataclass
class School:
    code: Optional[str] = None
    hakgudo_name: Optional[str] = None
    name: Optional[str] = None
    establish_divide: Optional[str] = None
    avg_students_per_class: Optional[str] = None
    distance: Optional[int] = None
    enter_seoul_university: Optional[str] = None
    enter_university: Optional[str] = None


@dataclass
class MiddleSchool:
    code: Optional[str] = None
    hakgudo_name: Optional[str] = None
    establish_divide: Optional[str] = None
    name: Optional[str] = None
    avg_students_per_class: Optional[str] = None
    total_enter_special_high_school: Optional[str] = None
    total_enter_autonomous_high_school: Optional[str] = None
    total_enter_special_high_school2: Optional[str] = None
    total_enter_autonomous_high_school2: Optional[str] = None
    distance: Optional[int] = None


@dataclass
class NurserySchool:
    code: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    child_per_teacher: Optional[str] = None
    certification_score: Optional[str] = None
    distance: Optional[int] = None


@dataclass
class Education:
    elementary_school: Optional[List[School]] = None
    nursery_school: Optional[List[NurserySchool]] = None
    middle_school: Optional[List[MiddleSchool]] = None
    high_school: Optional[List[School]] = None
    kinder_school: Optional[List[Any]] = None


@dataclass
class Image:
    image: Optional[str]
    image_title: Optional[str]
    image_desc: Optional[Any]
    location: Optional[List[float]]


@dataclass
class Complex:
    complex_id: Optional[str]
    complex_type: Optional[int]
    complex_name: Optional[str]
    household_num: Optional[int]
    building_num: Optional[int]
    parking_num: Optional[int]
    manage_tel: Optional[str]
    complex_lowest_floor: Optional[int]
    complex_highest_floor: Optional[int]
    build_cov_ratio: Optional[int]
    floor_area_index: Optional[int]
    provider_name: Optional[str]
    address: Optional[str]
    jibun_address: Optional[str]
    road_address: Optional[str]
    location: Optional[List[float]]
    parking_average: Optional[float]
    is_favorited: Optional[Any]
    favorited_count: Optional[int]
    is_default_image: Optional[bool]
    complex_type_str: Optional[str]
    parking_type_str: Optional[Any]
    heat_type_str: Optional[str]
    fuel_type_str: Optional[str]
    enter_date_str: Optional[str]
    represent_image: Optional[str]
    entrance_type_str: Optional[Any]
    real_price_max_trade: Optional[Any]
    real_price_min_trade: Optional[Any]
    real_price_max_lease: Optional[Any]
    real_price_min_lease: Optional[Any]
    maintenance_standard: Optional[str]
    maintenance_last_price: Optional[Any]
    maintenance_total_price: Optional[Any]
    maintenance_summer_total_price: Optional[Any]
    maintenance_winter_total_price: Optional[Any]
    trade_region_average_pyeong_price: Optional[Any]
    lease_region_average_pyeong_price: Optional[Any]
    trade_average_pyeong_price: Optional[Any]
    lease_average_pyeong_price: Optional[Any]
    images: Optional[List[Image]]


@dataclass
class Contact:
    call_number: Optional[str]
    sms_message: Optional[str]
    show_number: Optional[str]
    sms_number: Optional[str]


@dataclass
class DetailShop:
    use: Optional[bool]
    link: Optional[str]


@dataclass
class OtherRoom:
    is_favorited: Optional[Any]
    seq: Optional[int]
    id: Optional[str]
    user_id: Optional[str]
    status: Optional[int]
    deleted: Optional[bool]
    name: Optional[str]
    title: Optional[str]
    room_type: Optional[int]
    location: Optional[List[float]]
    random_location: Optional[List[float]]
    premium_badge: Optional[Any]
    hash_tags: Optional[List[str]]
    room_type_str: Optional[str]
    room_desc: Optional[str]
    img_url: Optional[str]
    img_urls: Optional[List[str]]
    is_pano: Optional[bool]
    price_title: Optional[str]
    selling_type: Optional[int]
    is_confirm: Optional[bool]
    confirm_type: Optional[Any]
    confirm_date_str: Optional[str]
    is_quick: Optional[bool]
    is_messenger_actived: Optional[bool]
    complex_name: Optional[str]


@dataclass
class ReviewElement:
    id: Optional[int]
    room_id: Optional[Any]
    agent_id: Optional[str]
    review_text: Optional[str]
    user_id: Optional[str]
    grade: Optional[int]
    has_comment: Optional[bool]
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
    seq: Optional[Any]
    user_active: Optional[bool]
    agent_profile_url: Optional[str]
    user_profile_url: Optional[str]


@dataclass
class DabangReview:
    review_count_good: Optional[int]
    reviews: Optional[List[ReviewElement]]
    review_count: Optional[int]


@dataclass
class DeungbonSummary:
    detailScore: Optional[str] = Field(
        ..., title="detail_score", alias="detailScore"
    )  # noqa
    regCommentTagMapList: Optional[List[Any]] = Field(
        ..., title="reg_comment_tag_map_list", alias="regCommentTagMapList"
    )  # noqa
    grade: Optional[int] = Field(...)
    grade_message: Optional[str] = Field(...)
    report_url: Optional[Any] = Field(...)
    report_date: Optional[str] = Field(...)


@dataclass
class Photo:
    key: Optional[str]
    desc: Optional[str]


@dataclass
class RoomOption:
    seq: Optional[int]
    name: Optional[str]


@dataclass
class Room:
    selling_type: SellingType
    is_favorited: Optional[Any] = None
    favorited_count: Optional[int] = None
    seq: Optional[int] = None
    id: Optional[str] = None
    user_id: Optional[str] = None
    status: Optional[int] = None
    title: Optional[str] = None
    memo: Optional[str] = None
    private_memo: Optional[Any] = None
    room_type: Optional[int] = None
    maintenance_option: Optional[int] = None
    room_size: Optional[float] = None
    provision_size: Optional[Any] = None
    pano: Optional[Any] = None
    moving_date: Optional[str] = None
    card: Optional[bool] = None
    photos: Optional[List[str]] = None
    photo: Optional[List[Photo]] = None
    price_info: Optional[List[List[int]]] = None
    address: Optional[str] = None
    location: Optional[List[float]] = None
    random_location: Optional[List[float]] = None
    shorten_url: Optional[str] = None
    agent_id: Optional[str] = None
    division: Optional[bool] = None
    duplex: Optional[bool] = None
    full_option: Optional[bool] = None
    complex_id: Optional[str] = None
    dong: Optional[str] = None
    ho: Optional[str] = None
    contract_size: Optional[float] = None
    enter_date: Optional[int] = None
    room_type_str: Optional[str] = None
    room_type_main_str: Optional[str] = None
    maintenance_items_str: Optional[List[str]] = None
    heating: Optional[str] = None
    room_floor_str: Optional[str] = None
    building_floor_str: Optional[str] = None
    maintenance_cost_str: Optional[str] = None
    full_options: Optional[List[str]] = None
    etc_options: Optional[List[str]] = None
    price_hash_tags: Optional[List[str]] = None
    option_hash_tags: Optional[List[str]] = None
    detail_hash_tags: Optional[List[str]] = None
    hash_tags: Optional[List[str]] = None
    price_title: Optional[str] = None
    price_info_str: Optional[List[List[str]]] = None
    animal_str: Optional[str] = None
    parking_str: Optional[str] = None
    elevator_str: Optional[str] = None
    loan_str: Optional[str] = None
    built_in_str: Optional[str] = None
    balcony_str: Optional[str] = None
    duplex_str: Optional[str] = None
    division_str: Optional[Any] = None
    short_lease_str: Optional[str] = None
    is_show: Optional[bool] = None
    is_show_new: Optional[bool] = None
    is_confirm: Optional[bool] = None
    confirm_type: Optional[Any] = None
    confirm_date_str: Optional[str] = None
    is_quick: Optional[Any] = None
    month_total_str: Optional[str] = None
    month_total_cost_str: Optional[str] = None
    building_use: Optional[Any] = None
    deungbon_summary: Optional[DeungbonSummary] = None
    beds_num: Optional[int] = None
    bath_num: Optional[int] = None
    show_watermark: Optional[bool] = None
    room_options: Optional[List[RoomOption]] = None
    safeties: Optional[List[RoomOption]] = None


@dataclass
class Average:
    price: Optional[float] = None
    options: Optional[int] = None
    near: Optional[int] = None
    maintenance: Optional[int] = None
    traffic: Optional[int] = None


@dataclass
class Score:
    average: Optional[Average] = None
    total: Optional[float] = None
    message: Optional[str] = None
    room: Optional[Average] = None


@dataclass
class Shinhanbank:
    deposit: Optional[int] = None
    location: Optional[int] = None


@dataclass
class Space:
    space_seq: Optional[int] = None
    pyeong_type: Optional[str] = None
    pyeong: Optional[int] = None
    household_num: Optional[int] = None
    beds_num: Optional[int] = None
    bath_num: Optional[int] = None
    exclusive_space: Optional[float] = None
    supply_space: Optional[Any] = None
    contract_space: Optional[float] = None
    entrance_type_str: Optional[str] = None
    real_price_max_trade: Optional[Any] = None
    real_price_min_trade: Optional[Any] = None
    real_price_max_lease: Optional[Any] = None
    real_price_min_lease: Optional[Any] = None
    has_trade_real_price: Optional[bool] = None
    has_lease_real_price: Optional[bool] = None
    maintenance_last_price: Optional[Any] = None
    maintenance_total_price: Optional[Any] = None
    maintenance_summer_total_price: Optional[Any] = None
    maintenance_winter_total_price: Optional[Any] = None
    maintenance_total_price_str: Optional[str] = None
    layout_image: Optional[str] = None
    extend_layout_image: Optional[Any] = None


@dataclass
class User:
    idx: Optional[int] = None
    email: Optional[str] = None
    name: Optional[str] = None
    active: Optional[bool] = None
    inquery_phone: Optional[str] = None
    phone: Optional[str] = None
    tel: Optional[str] = None
    safe_phone: Optional[str] = None
    yellow_id: Optional[Any] = None
    is_subscribe: Optional[bool] = None
    position: Optional[Any] = None
    profile_url: Optional[str] = None
    message: Optional[str] = None
    role_type: Optional[str] = None


@dataclass
class Dabang:
    is_messenger_sender_agented: Optional[bool] = None
    ios_score_height: Optional[int] = None
    agent: Optional[Agent] = None
    education: Optional[Education] = None
    detail_shop: Optional[DetailShop] = None
    bubble_image: Optional[Any] = None
    room: Optional[Room] = None
    is_messenger_actived: Optional[bool] = None
    score: Optional[Score] = None
    review: Optional[DabangReview] = None
    is_messenger_receipted: Optional[bool] = None
    contact: Optional[Contact] = None
    other_rooms: Optional[List[OtherRoom]] = None
    shinhanbank: Optional[Shinhanbank] = None
    messenger_send_alimtalk_contents: Optional[str] = None
    user: Optional[User] = None
    messenger_bubble_contents: Optional[str] = None
    complex: Optional[Complex] = None
    space: Optional[Space] = None

    def to_room(self) -> RoomItem:
        if self.room is None:
            raise NoneTypeError("방 정보가 없습니다")
        if self.room.room_type is None:
            raise NoneTypeError("방 유형이 없습니다")
        if self.room.price_info is None:
            raise NoneTypeError("방 가격 정보가 없습니다")
        if self.room.photos is None:
            raise NoneTypeError("방 사진이 없습니다")
        deposit, monthly_rent, _ = self.room.price_info.pop()
        image_key = self.room.photos.pop()

        return RoomItem(
            uid=f"Dabang::{self.room.id}",
            deposit=deposit,
            monthly_rent=monthly_rent,
            selling_type=SellingType(self.room.selling_type),
            address=self.room.address,
            title=self.room.title,
            description=self.room.memo,
            image=image_url.format(image_key=image_key),
            building_type=BuildingType(self.room.room_type),
        )
