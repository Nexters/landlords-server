from typing import List, Optional

from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import Enum

from ....core.database import Base
from ...persona.models.domain import QuestionType
from ...persona.models.entity import ChoiceItem
from ...rooms.models.entity import Room
from ...users.models.entity import User
from .domain import Contents, Label, StatusCategory, Title


class CheckItem(Base):
    """ 선택 항목 """

    __tablename__ = "checklist_items"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    uid: int = Column(
        mysql.BIGINT(20, unsigned=True), primary_key=True, comment="고유 식별자"
    )

    contents: str = Column(
        "contents",
        mysql.VARCHAR(Contents.max_length),
        nullable=True,
        comment="선택지 내용",
    )

    question_id: int = Column(
        "question_id",
        ForeignKey(
            "checklist_questions.uid", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        comment="질문지 고유 식별자",
    )
    question: Optional["CheckQuestion"] = relationship(
        "CheckQuestion",
        uselist=False,
        primaryjoin="CheckItem.question_id==CheckQuestion.uid",
        backref="checklist_questions",
    )

    def __init__(
        self,
        uid: int,
        contents: str,
        question_id: int,
        image_url: str,
        question: Optional["CheckQuestion"] = None,
    ) -> None:
        self.uid = uid
        self.contents = contents
        self.question_id = question_id
        self.image_url = image_url
        self.question = question


class CheckAnswer(Base):
    """ 문제에 대한 선택 """

    __tablename__ = "checklist_answers"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    user_id: int = Column(
        "user_id",
        ForeignKey("users.uid", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    respondent: User = relationship(
        "User",
        uselist=False,
        primaryjoin="CheckAnswer.user_id==User.uid",
        backref="checklist_answers",
    )

    room_id: str = Column(
        "room_id",
        ForeignKey("rooms.uid", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    room: Room = relationship(
        "Room",
        uselist=False,
        primaryjoin="CheckAnswer.room_id==Room.uid",
        backref="checklist_answers",
    )

    check_id: int = Column(
        "check_id",
        ForeignKey(
            "checklist_items.uid", ondelete="CASCADE", onupdate="CASCADE"
        ),
        primary_key=True,
    )
    check: CheckItem = relationship(
        "CheckItem",
        uselist=False,
        primaryjoin="CheckAnswer.check_id==CheckItem.uid",
        backref="checklist_answers",
    )

    created = Column(
        "Created",
        mysql.DATETIME(),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="생성일자",
    )

    def __init__(self, user_id: int, check_id: int, room_id: str) -> None:
        self.user_id = user_id
        self.check_id = check_id
        self.room_id = room_id


class CheckQuestion(Base):
    """ 체크리스트 """

    __tablename__ = "checklist_questions"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    uid: int = Column(
        "uid",
        mysql.BIGINT(20, unsigned=True),
        primary_key=True,
        comment="고유 식별자",
    )

    title: str = Column(
        "title",
        mysql.VARCHAR(Title.max_length),
        nullable=False,
        comment="체크리스트 질문",
    )

    type_: QuestionType = Column(
        "type_", Enum(QuestionType), nullable=False, comment="질문 유형"
    )

    label: str = Column(
        "label",
        mysql.VARCHAR(Label.max_length),
        nullable=False,
        comment="질문 라벨",
    )

    status: str = Column(
        "status", Enum(StatusCategory), nullable=False, comment="방 계약 상태"
    )

    checks: List[CheckItem] = relationship(
        "CheckItem",
        uselist=True,
        primaryjoin="CheckQuestion.uid==CheckItem.question_id",
        backref="checklist_questions",
    )

    choice_id: int = Column(
        "choice_id",
        ForeignKey(
            "persona_choices.uid", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=True,
        comment="체크리스트 질문과 맵핑되는 페르소나 선택지",
    )

    choice: Optional[ChoiceItem] = relationship(
        "ChoiceItem",
        uselist=False,
        primaryjoin="CheckQuestion.choice_id==ChoiceItem.uid",
        backref="checklist_questions",
    )

    def __init__(
        self,
        title: str,
        type_: QuestionType,
        label: str,
        status: StatusCategory,
        choice_id: int,
    ) -> None:
        self.title = title
        self.type_ = type_
        self.label = label
        self.status = status
        self.choice_id = choice_id


class UserChecklist(Base):
    __tablename__ = "users_checklist"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    user_id: int = Column(
        "user_id",
        ForeignKey("users.uid", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    user: User = relationship(
        "User",
        uselist=False,
        primaryjoin="UserChecklist.user_id==User.uid",
        backref="users_checklist",
    )

    question_id: int = Column(
        "question_id",
        ForeignKey(CheckQuestion.uid, ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )

    question: CheckQuestion = relationship(
        "CheckQuestion",
        uselist=False,
        primaryjoin="UserChecklist.question_id==CheckQuestion.uid",
        backref="users_checklist",
    )

    def __init__(self, user_id: int, question_id: int) -> None:
        self.user_id = user_id
        self.question_id = question_id
