from typing import List

from pydantic import BaseModel, Field

from ...persona.models.domain import QuestionCategory, QuestionType
from .entity import Contents, Label, Title


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class CheckItem(OrmModel):
    """ 체크리스트 선택항목"""

    uid: int
    question_id: int
    contents: str = Field(max_length=Contents.max_length)


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
    category: QuestionCategory
    checks: List[CheckItem]


class UserChecklist(OrmModel):
    user_id: int
    questions: List[CheckQuestion]
