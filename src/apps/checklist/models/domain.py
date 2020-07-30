from typing import List

from pydantic import BaseModel

from ...persona.models.domain import QuestionCategory, QuestionType


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class CheckItem(OrmModel):
    """ 체크리스트 선택항목"""

    uid: int
    question_id: int
    contents: str


class CheckAnswer(OrmModel):
    """ 선택한 체크항목 """

    user_id: int
    room_id: str
    check: CheckItem


class CheckQuestion(OrmModel):
    """ 체크리스트 질문 """

    uid: int
    title: str
    type_: QuestionType
    label: str
    category: QuestionCategory
    checks: List[CheckItem]


class UserChecklist(OrmModel):
    user_id: int
    questions: List[CheckQuestion]
