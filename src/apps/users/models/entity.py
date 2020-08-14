from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import func
from sqlalchemy.types import Enum

from ....core.database import Base
from ...oauth.models.domain.landlords import OAuthType


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    uid = Column(
        "uid",
        mysql.BIGINT(20, unsigned=True),
        primary_key=True,
        autoincrement=True,
        comment="유저 id",
    )
    oauth_type = Column(
        "oauth_type", Enum(OAuthType), nullable=False, comment="인증 서비스 유형"
    )
    sub = Column("sub", mysql.VARCHAR(100), comment="구글 uid")
    email = Column(
        "Email",
        mysql.VARCHAR(50),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="이메일",
        index=True,
    )
    full_name = Column(
        "FullName",
        mysql.VARCHAR(32),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="전체 이름",
    )
    profile = Column(
        "Profile",
        mysql.VARCHAR(300),
        nullable=True,
        default="",
        server_default=text("''"),
        comment="프로필 사진",
    )

    disabled = Column(
        "Disabled",
        mysql.TINYINT(1),
        nullable=True,
        default=0,
        server_default=text("0"),
        comment="사용자 활성화 여부 (0: enable, 1: disable)",
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
        sub: str,
        oauth_type: OAuthType,
        email: str,
        name: str,
        picture: str,
        disabled: bool,
    ) -> None:
        self.sub = sub
        self.oauth_type = oauth_type
        self.email = email
        self.full_name = name
        self.profile = picture
        self.disabled = int(disabled)
