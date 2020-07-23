from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import func

from ...core.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    at_hash = Column(
        "at_hash", mysql.VARCHAR(100), primary_key=True, comment="구글 hash"
    )
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
        at_hash: str,
        email: str,
        full_name: str,
        profile: str,
        disabled: bool,
    ) -> None:
        self.at_hash = at_hash
        self.email = email
        self.full_name = full_name
        self.profile = profile
        self.disabled = int(disabled)
