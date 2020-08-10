from typing import List

from fastapi import status
from fastapi.param_functions import Depends, Security
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from ...core.database import get_database_session
from ..oauth.models.domain.landlords import UserInDB
from ..oauth.services import get_current_user
from . import services
from .models.domain import ChoiceItem as ChoiceItemDto
from .models.domain import Question as QuestionDto
from .models.entity import ChoiceItem, Question, QuestionAnswer
from .models.responses import PersonaQuestionsResponse, PersonaResponse

router = APIRouter()


@router.get(
    path="/questions",
    name="페르소나 분석 질문 리스트",
    status_code=status.HTTP_200_OK,
    response_model=PersonaQuestionsResponse,
)
async def get_questions(
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> PersonaQuestionsResponse:
    """ 페르소나 분석 질문 리스트 """
    questions = (
        session.query(Question)
        .join(ChoiceItem, ChoiceItem.question_id == Question.uid)
        .all()
    )
    return PersonaQuestionsResponse(
        questions=[QuestionDto.from_orm(question) for question in questions]
    )


@router.post(
    path="/answers",
    name="페르소나 질문 응답 저장",
    status_code=status.HTTP_201_CREATED,
    response_model=List[ChoiceItemDto],
)
async def post_answers(
    choices: List[int],
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> List[ChoiceItemDto]:
    answers = [
        QuestionAnswer(user_id=current_user.uid, choice_id=choice_id)
        for choice_id in choices
    ]
    for answer in answers:
        session.add(answer)
        session.flush()
        session.refresh(answer)
    session.commit()
    return [ChoiceItemDto.from_orm(answer.choice) for answer in answers]


@router.get(
    path="",
    name="나의 페르소나",
    status_code=status.HTTP_200_OK,
    response_model=PersonaResponse,
)
async def get_persona(
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> PersonaResponse:
    """ 나의 페르소나

    페르소나 분석 결과
    """
    persona = services.get_persona(
        answers=services.get_user_choices(
            user_info=current_user, session=session
        )
    )
    return PersonaResponse(title=persona.name, description=persona.value)
