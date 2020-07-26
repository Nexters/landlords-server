from typing import List

from sqlalchemy.orm import Session

from ..oauth.entity import User
from ..oauth.models import UserInfo
from ..persona.models.domain import ChoiceItem, QuestionCategory, QuestionType
from .models.domain import CheckQuestion


def get_checklist(
    answers: List[ChoiceItem], session: Session
) -> List[CheckQuestion]:

    checkQuestions: List[CheckQuestion] = (session.query(CheckQuestion).all())
    return checkQuestions
