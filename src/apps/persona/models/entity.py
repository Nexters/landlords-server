from enum import IntEnum
from typing import List, Optional

from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import Enum

from ....core.database import Base
from ...users.models.entity import User
from .domain import QuestionCategory, QuestionType


class Url(IntEnum):

    max_length = 500


class Contents(IntEnum):
    max_length = 100


class Title(IntEnum):
    max_length = 50


class ChoiceItem(Base):
    """ 선택 항목 """

    __tablename__ = "persona_choices"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    uid: Optional[int] = Column(
        "uid",
        mysql.BIGINT(20, unsigned=True),
        primary_key=True,
        comment="고유 식별자",
    )

    contents: str = Column(
        "contents",
        mysql.VARCHAR(Contents.max_length),
        nullable=False,
        comment="선택지 내용",
    )
    category: QuestionCategory = Column(
        "category",
        Enum(QuestionCategory),
        nullable=False,
        comment="집 선택 시 더 가치를 두는 카테고리",
    )

    question_id: int = Column(
        "question_id",
        ForeignKey(
            "persona_questions.uid", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        comment="질문지 고유 식별자",
    )
    question: Optional["Question"] = relationship(
        "Question",
        uselist=False,
        primaryjoin="ChoiceItem.question_id==Question.uid",
        backref="persona_choices",
    )

    image_url: str = Column(
        "image_url",
        mysql.VARCHAR(Url.max_length),
        nullable=False,
        comment="일러스트 url",
    )

    def __init__(
        self,
        contents: str,
        category: QuestionCategory,
        question_id: int,
        image_url: str,
        question: Optional["Question"] = None,
        uid: Optional[int] = None,
    ) -> None:
        self.contents = contents
        self.category = category
        self.question_id = question_id
        self.image_url = image_url
        self.question = question
        self.uid = uid


class QuestionAnswer(Base):
    """ 문제에 대한 선택 """

    __tablename__ = "persona_answers"
    __table_args__ = {"mysql_collate": "utf8mb4_unicode_ci"}

    user_id: int = Column(
        "user_id",
        ForeignKey("users.uid", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    respondent: User = relationship(
        "User",
        uselist=False,
        primaryjoin="QuestionAnswer.user_id==User.uid",
        backref="persona_answer",
    )

    choice_id: int = Column(
        "choice_id",
        ForeignKey(
            "persona_choices.uid", ondelete="CASCADE", onupdate="CASCADE"
        ),
        primary_key=True,
    )
    choice: ChoiceItem = relationship(
        "ChoiceItem",
        uselist=False,
        primaryjoin="QuestionAnswer.choice_id==ChoiceItem.uid",
        backref="persona_answer",
        lazy="joined",
    )

    created = Column(
        "Created",
        mysql.DATETIME(),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="생성일자",
    )

    def __init__(self, user_id: int, choice_id: int) -> None:
        self.user_id = user_id
        self.choice_id = choice_id


class Question(Base):
    """ 질문 리스트 """

    __tablename__ = "persona_questions"
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
        comment="질문 내용",
    )
    type_: QuestionType = Column(
        "type_", Enum(QuestionType), nullable=False, comment="질문 유형"
    )
    choices: List[ChoiceItem] = relationship(
        "ChoiceItem",
        uselist=True,
        primaryjoin="Question.uid==ChoiceItem.question_id",
        backref="persona_questions",
    )

    def __init__(self, title: str, type_: QuestionType) -> None:
        self.title = title
        self.type_ = type_
