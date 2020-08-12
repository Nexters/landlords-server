from enum import Enum
from typing import List

from pydantic import BaseModel


class Persona(str, Enum):
    """ 페르소나 """

    핵인싸 = "일주일에 4번 이상 약속있는"
    밖순이 = "나가서 노는걸 좋아하는"
    부르면_나감 = "굳이 약속을 잡진 않지만"
    집순이 = "웬만하면 잘 안나가는"


class QuestionType(str, Enum):
    """ 문제 유형 """

    SingleChoice = "SingleChoice"
    MultipleChoice = "MultipleChoice"


class QuestionCategory(str, Enum):
    """ 질문 카테고리 - 페르소나 분석 용 카테고리

        Normal 일반

        Welfare 복지

        Transportation 교통

        Economical 경제
    """

    Normal = "Normal"
    Welfare = "Welfare"
    Transportation = "Transportation"
    Economical = "Economical"


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class ChoiceItem(OrmModel):
    """ 선택 항목 - 사용자가 선택한 항목에 따라 자동으로 제공되는 추천 체크리스트 항목 변화

        uid: 고유 식별자

        question_id: 문제 고유 식별자

        content: 내용
    """

    uid: int
    question_id: int
    contents: str
    category: QuestionCategory


class QuestionAnswer(OrmModel):
    """ 문제에 대한 선택 """

    user_id: int
    choice: ChoiceItem


class Question(OrmModel):
    """ 문제 """

    uid: int
    title: str
    choices: List[ChoiceItem]

    type_: QuestionType
