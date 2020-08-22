from enum import IntEnum

from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.types import Enum

from .....core.database import Base
from ....users.models.entity import User
from ..domain.landlords import (
    Address,
    AdministrativeExpenses,
    BuildingType,
    Description,
    Floor,
    Image,
    RoomSize,
    SellingType,
    Title,
    Uid,
)


class Room(Base):
    """ 방 entity

    [부동산 관련 field명 참고 자료](https://news.joins.com/article/23191326)
    """

    __tablename__ = "rooms"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    uid = Column(
        "uid",
        mysql.VARCHAR(Uid.max_length),
        primary_key=True,
        comment="방의 고유ID",
    )
    user_id: int = Column(
        "user_id",
        ForeignKey("users.uid", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    user: User = relationship(
        "User",
        uselist=False,
        primaryjoin="Room.user_id==User.uid",
        backref="user_rooms",
    )

    deposit = Column(
        "deposit",
        mysql.INTEGER(unsigned=True),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="보증금",
    )

    monthly_rent = Column(
        "monthly_rent",
        mysql.INTEGER(unsigned=True),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="월세",
    )

    selling_type = Column(
        "selling_type", Enum(SellingType), nullable=False, comment="매매타입"
    )

    address = Column(
        "address",
        mysql.VARCHAR(Address.max_length),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="주소",
    )

    title = Column(
        "title",
        mysql.VARCHAR(Title.max_length),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="제목",
    )

    description = Column(
        "description",
        mysql.VARCHAR(Description.max_length),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="방에 대한 간략한 설명",
    )

    building_type = Column(
        "building_type", Enum(BuildingType), nullable=False, comment="방 유형"
    )

    image = Column(
        "image",
        mysql.VARCHAR(Image.max_length),
        nullable=True,
        comment="방의 Image URL",
    )

    room_size = Column(
        "room_size",
        mysql.DOUBLE(
            int(RoomSize.max_precision), int(RoomSize.max_scale), unsigned=True
        ),
        comment="방 크기 (㎡)",
    )

    floor = Column("floor", mysql.VARCHAR(Floor.max_length), comment="층/건물층수")

    has_elevator = Column(
        "has_elevator", mysql.TINYINT(1), nullable=True, comment="엘리베이터 유무"
    )

    administrative_expenses = Column(
        "administrative_expenses",
        mysql.TINYINT(int(AdministrativeExpenses.max_length), unsigned=True),
        comment="관리비",
    )

    created = Column(
        "Created",
        mysql.DATETIME(),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="생성일자",
    )

    updated = Column(
        "Updated",
        mysql.DATETIME(),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        onupdate=func.now(),
        comment="마지막 수정시간",
    )

    def __init__(
        self,
        uid: str,
        user_id: int,
        deposit: int,
        monthly_rent: int,
        selling_type: SellingType,
        address: str,
        title: str,
        description: str,
        image: str,
        building_type: BuildingType,
        room_size: float,
        floor: str,
        has_elevator: bool,
        administrative_expenses: int,
    ) -> None:
        self.uid = uid
        self.user_id = user_id
        self.deposit = deposit
        self.monthly_rent = monthly_rent
        self.selling_type = selling_type
        self.address = address
        self.title = title
        self.description = description
        self.image = image
        self.building_type = building_type
        self.room_size = room_size
        self.floor = floor
        self.has_elevator = has_elevator
        self.administrative_expenses = administrative_expenses
