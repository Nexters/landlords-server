from typing import List

from sqlalchemy.orm import Session

from ..persona.models.entity import ChoiceItem
from ..persona.models.entity import QuestionAnswer as PersonaQuestionAnswer
from ..persona.services import delete_if_existed
from ..users.models.domain import UserInDB
from .models.domain import CheckQuestion as CheckQuestionDto
from .models.domain import StatusCategory
from .models.entity import CheckItem, CheckQuestion


def get_checklist(
    user_info: UserInDB, session: Session, status: StatusCategory
) -> List[CheckQuestionDto]:
    """사용자의 체크리스트 가져오기"""
    delete_if_existed(user_info, session)
    checklist_from_answers_query = (
        session.query(
            PersonaQuestionAnswer, ChoiceItem, CheckQuestion, CheckItem
        )
        .join(PersonaQuestionAnswer.choice)
        .join(ChoiceItem.check_questions, isouter=True)
        .filter(
            (PersonaQuestionAnswer.user_id == user_info.uid)
            & (CheckQuestion.status == status)
        )
        .with_entities(CheckQuestion)
    )
    common_questions_query = (
        session.query(
            PersonaQuestionAnswer, ChoiceItem, CheckQuestion, CheckItem
        )
        .filter(
            (CheckQuestion.choice_id == (None))
            & (CheckQuestion.status == status)
        )
        .with_entities(CheckQuestion)
    )
    checklists: List[CheckQuestion] = checklist_from_answers_query.union_all(
        common_questions_query
    ).all()

    return [
        CheckQuestionDto.from_orm(checklist)
        for checklist in checklists
        if checklist
    ]
