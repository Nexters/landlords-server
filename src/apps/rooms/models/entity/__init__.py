from enum import IntEnum

from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import func

from .....core.database import Base


class Description(IntEnum):
    max_length = 200


class Uid(IntEnum):
    max_length = 100


class Address(IntEnum):
    max_length = 100


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

    is_jeonse = Column(
        "is_jeonse",
        mysql.TINYINT(unsigned=True),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="전세유무",
    )

    address = Column(
        "address",
        mysql.VARCHAR(Address.max_length),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="주소",
    )

    description = Column(
        "description",
        mysql.VARCHAR(Description.max_length),
        nullable=False,
        default="0",
        server_default=text("0"),
        comment="방에 대한 간략한 설명",
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
        deposit: int,
        monthly_rent: int,
        is_jeonse: bool,
        address: str,
        description: str,
    ) -> None:
        self.uid = uid
        self.deposit = deposit
        self.monthly_rent = monthly_rent
        self.is_jeonse = int(is_jeonse)
        self.address = address
        self.description = description
