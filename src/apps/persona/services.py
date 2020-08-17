from typing import List, Optional

from sqlalchemy.orm import Session

from ..users.models.domain import UserInfo
from ..users.models.entity import User
from .models.domain import ChoiceItem as ChoiceItemDto
from .models.domain import Persona
from .models.domain import QuestionAnswer as QuestionAnswerDto
from .models.entity import QuestionAnswer


def get_persona(check_answers: List[int]) -> Persona:
    """ 사용자 페르소나 분석 """

    question1 = check_answers[0]
    question2 = check_answers[5]
    question3 = check_answers[8]

    if (question1 == 1) & (question2 == 1) & (question3 == 1):
        result = Persona.PRO_LIVING_ALONE
    elif (question1 == 1) & (question2 == 1) & (question3 == 2):
        result = Persona.INSIDER
    elif (question1 == 1) & (question2 == 2) & (question3 == 2):
        result = Persona.SMART
    elif (question1 == 2) & (question2 == 1) & (question3 == 1):
        result = Persona.PLAYPLAY_DODO
    elif (question1 == 2) & (question2 == 2) & (question3 == 1):
        result = Persona.HOMEBODY
    elif (question1 == 2) & (question2 == 2) & (question3 == 2):
        result = Persona.IM_FIRST

    return result


def get_user_choices(
    user_info: UserInfo, session: Session
) -> List[ChoiceItemDto]:
    answers: List[Optional[QuestionAnswer]] = (
        session.query(User)
        .filter_by(email=user_info.email)
        .outerjoin(QuestionAnswer, QuestionAnswer.user_id == User.uid)
        .with_entities(QuestionAnswer)
        .all()
    )
    answers_: List[ChoiceItemDto] = (
        []
        if None in answers
        else [QuestionAnswerDto.from_orm(answer).choice for answer in answers]
    )
    return answers_
