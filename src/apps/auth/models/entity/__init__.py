from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql

from .....core.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    id = Column(
        "id",
        mysql.INTEGER,
        primary_key=True,
        comment="고유 id",
        autoincrement=True,
    )
    email = Column(
        "Email",
        mysql.VARCHAR(50),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="이메일",
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

    def __init__(
        self, email: str, full_name: str, profile: str, disabled: bool
    ) -> None:
        self.email = email
        self.full_name = full_name
        self.profile = profile
        self.disabled = int(disabled)
