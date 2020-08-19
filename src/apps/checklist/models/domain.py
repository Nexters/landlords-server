from enum import Enum, IntEnum
from typing import List, Optional

from pydantic import BaseModel, Field

from ...persona.models.domain import QuestionType


class Contents(IntEnum):
    max_length = 100


class Title(IntEnum):
    max_length = 50


class Label(IntEnum):
    max_length = 50


class StatusCategory(str, Enum):
    """ 문제 유형 """

    Looking = "Looking"
    Contracting = "Contracting"
    Moving = "Moving"


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class CheckItem(OrmModel):
    """ 체크리스트 선택항목"""

    uid: int
    question_id: int
    contents: Optional[str] = Field(
        default=None, max_length=Contents.max_length
    )


class CheckAnswer(OrmModel):
    """ 선택한 체크항목 """

    user_id: int
    room_id: str
    check: CheckItem


class CheckQuestion(OrmModel):
    """ 체크리스트 질문 """

    uid: int
    title: str = Field(max_length=Title.max_length)
    type_: QuestionType
    label: str = Field(max_length=Label.max_length)
    status: StatusCategory
    checks: List[CheckItem]
