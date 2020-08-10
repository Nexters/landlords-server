from typing import List

from sqlalchemy.orm import Session

from ..oauth.models.domain.landlords import UserInDB
from ..persona.models.domain import ChoiceItem
from ..persona.services import get_user_choices
from .models.domain import CheckQuestion as CheckQuestionDto
from .models.domain import StateCategory
from .models.entity import CheckQuestion, UserChecklist


def get_checklist(
    user_info: UserInDB, session: Session, state: StateCategory
) -> List[CheckQuestionDto]:
    """사용자의 체크리스트 가져오기"""
    user_checklist: List[CheckQuestionDto] = (
        session.query(CheckQuestion)
        .join(UserChecklist, CheckQuestion.uid == UserChecklist.question_id)
        .filter(
            (UserChecklist.user_id == user_info.uid)
            & (CheckQuestion.state == state)
        )
        .all()
    )

    if not user_checklist:
        user_checklist = get_checklist_by_persona(
            answers=get_user_choices(user_info=user_info, session=session),
            session=session,
            state=state,
        )

        for question in user_checklist:
            user_checklist_: UserChecklist = UserChecklist(
                user_id=user_info.uid, question_id=question.uid
            )
            session.add(user_checklist_)
        session.commit()

    return user_checklist


def get_checklist_by_persona(
    answers: List[ChoiceItem], session: Session, state: StateCategory
) -> List[CheckQuestionDto]:
    """페르소나 태그를 통해 체크리스트 질문 필터링"""
    checklist: List[CheckQuestionDto] = session.query(CheckQuestion).filter(
        CheckQuestion.state == state
    ).all()
    return checklist
