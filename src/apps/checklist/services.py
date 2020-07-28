from typing import List

from sqlalchemy.orm import Session

from ..oauth.entity import User
from ..oauth.models import UserInfo
from ..persona.models.domain import ChoiceItem, QuestionCategory, QuestionType
from .models.domain import Checklist
from .models.entity import CheckItem, CheckQuestion


def get_checklist(answers: List[ChoiceItem], session: Session) -> Checklist:
    """페르소나 태그를 통해 체크리스트 질문 필터링"""

    checkQuestions: Checklist = (
        session.query(CheckQuestion)
        .join(CheckItem, CheckItem.question_id == CheckQuestion.uid)
        .all()
    )
    return checkQuestions
