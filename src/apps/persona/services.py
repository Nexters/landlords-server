from typing import List

from sqlalchemy.orm import Session

from ..oauth.entity import User
from ..oauth.models import UserInfo
from .models.domain import ChoiceItem as ChoiceItemDto
from .models.domain import Persona
from .models.domain import QuestionAnswer as QuestionAnswerDto
from .models.entity import ChoiceItem, QuestionAnswer


def get_persona(answers: List[ChoiceItemDto]) -> Persona:
    """ 사용자 페르소나 분석 """
    return Persona.핵인싸


def get_user_choices(
    user_info: UserInfo, session: Session
) -> List[ChoiceItemDto]:
    answers: List[QuestionAnswer] = (
        session.query(QuestionAnswer)
        .join(User, User.uid == QuestionAnswer.user_id)
        .join(ChoiceItem, QuestionAnswer.choice_id == ChoiceItem.uid)
        .filter(User.email == user_info.email)
        .all()
    )
    answers_: List[ChoiceItemDto] = [
        QuestionAnswerDto.from_orm(answer).choice for answer in answers
    ]
    return answers_
