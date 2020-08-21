from typing import List, Optional

from sqlalchemy.orm import Session

from ..checklist.models.entity import CheckAnswer
from ..rooms.models.entity import Room
from ..users.models.domain import UserInDB, UserInfo
from ..users.models.entity import User
from .models.domain import ChoiceItem as ChoiceItemDto
from .models.domain import Persona
from .models.domain import QuestionAnswer as QuestionAnswerDto
from .models.entity import QuestionAnswer


def get_persona(check_answers: List[int]) -> Persona:
    """ 사용자 페르소나 분석 """

    question1 = is_first_or_second(check_answers[0])
    question2 = is_first_or_second(check_answers[5])
    question3 = is_first_or_second(check_answers[8])

    result = Persona.INSIDER

    if (
        (question1 == "FIRST") & (question2 == "FIRST") & (question3 == "FIRST")
    ) | (
        (question1 == "FIRST")
        & (question2 == "SECOND")
        & (question3 == "FIRST")
    ):
        result = Persona.PRO_LIVING_ALONE
    elif (
        (question1 == "FIRST")
        & (question2 == "FIRST")
        & (question3 == "SECOND")
    ):
        result = Persona.INSIDER
    elif (
        (question1 == "FIRST")
        & (question2 == "SECOND")
        & (question3 == "SECOND")
    ):
        result = Persona.SMART
    elif (
        (question1 == "SECOND")
        & (question2 == "FIRST")
        & (question3 == "FIRST")
    ):
        result = Persona.PLAYPLAY_DODO
    elif (
        (question1 == "SECOND")
        & (question2 == "SECOND")
        & (question3 == "FIRST")
    ):
        result = Persona.HOMEBODY
    elif (
        (question1 == "SECOND")
        & (question2 == "SECOND")
        & (question3 == "SECOND")
    ):
        result = Persona.IM_FIRST

    return result


def is_first_or_second(choice_id: int) -> str:
    return "FIRST" if choice_id <= 10 else "SECOND"


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


def delete_if_existed(current_user: UserInDB, session: Session) -> None:
    persona_answers: QuestionAnswer = (
        session.query(QuestionAnswer)
        .filter(QuestionAnswer.user_id == current_user.uid)
        .all()
    )

    if persona_answers:
        for answer in persona_answers:
            session.delete(answer)

    checklist_answers: CheckAnswer = (
        session.query(CheckAnswer)
        .filter(CheckAnswer.user_id == current_user.uid)
        .all()
    )

    if checklist_answers:
        for answer in checklist_answers:
            session.delete(answer)

    rooms: Room = (
        session.query(Room).filter(Room.user_id == current_user.uid).all()
    )

    if rooms:
        for room in rooms:
            session.delete(room)
