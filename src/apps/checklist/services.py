from typing import List

from sqlalchemy.orm import Session

from ..persona.models.entity import QuestionAnswer
from ..users.models.domain import UserInDB
from .models.domain import CheckQuestion as CheckQuestionDto
from .models.domain import StatusCategory
from .models.entity import CheckQuestion


def get_checklist(
    user_info: UserInDB, session: Session, status: StatusCategory
) -> List[CheckQuestionDto]:
    """사용자의 체크리스트 가져오기"""

    checklist: List[CheckQuestionDto] = session.query(CheckQuestion).filter(
        (CheckQuestion.status == status)
        & (
            (QuestionAnswer.user_id == user_info.uid)
            | (CheckQuestion.choice_id == (None))
        )
    ).outerjoin(
        QuestionAnswer, QuestionAnswer.choice_id == CheckQuestion.choice_id
    ).all()

    return checklist
