from enum import Enum
from typing import List

from pydantic import BaseModel

from . import const


class RecommendedPlace(str, Enum):
    """추천 공간"""

    ONEROOM = "원룸"
    OFFICETEL = "오피스텔"
    MIXED_USE_BUILDING = "주상복합"
    SEPERATED_ONEROOM = "분리형 원룸"
    SIA_ONEROOM = "초역세권 원룸"
    NEW_ONEROOM = "신축 원룸"


class Persona(Enum):
    """ 페르소나 """

    HOMEBODY = {
        "type": const.PERSONA_RESULT_HOMEBODY,
        "description": const.PERSONA_DESCRIPTION_HOMEBODY,
        "recommended_place": [
            RecommendedPlace.OFFICETEL,
            RecommendedPlace.MIXED_USE_BUILDING,
        ],
    }
    PRO_LIVING_ALONE = {
        "type": const.PERSONA_RESULT_PRO_LIVING_ALONE,
        "description": const.PERSONA_DESCRIPTION_PRO_LIVING_ALONE,
        "recommended_place": [RecommendedPlace.SEPERATED_ONEROOM],
    }
    SMART = {
        "type": const.PERSONA_RESULT_SMART,
        "description": const.PERSONA_DESCRIPTION_SMART,
        "recommended_place": [
            RecommendedPlace.ONEROOM,
            RecommendedPlace.MIXED_USE_BUILDING,
        ],
    }
    PLAYPLAY_DODO = {
        "type": const.PERSONA_RESULT_PLAYPLAY_DODO,
        "description": const.PERSONA_DESCRIPTION_PLAYPLAY_DODO,
        "recommended_place": [
            RecommendedPlace.NEW_ONEROOM,
            RecommendedPlace.OFFICETEL,
        ],
    }
    IM_FIRST = {
        "type": const.PERSONA_RESULT_IM_FIRST,
        "description": const.PERSONA_DESCRIPTION_IM_FIRST,
        "recommended_place": [RecommendedPlace.OFFICETEL],
    }
    INSIDER = {
        "type": const.PERSONA_RESULT_INSIDER,
        "description": const.PERSONA_DESCRIPTION_INSIDER,
        "recommended_place": [RecommendedPlace.SIA_ONEROOM],
    }


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
