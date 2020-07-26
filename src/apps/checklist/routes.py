from typing import List

from fastapi import status
from fastapi.param_functions import Depends, Security
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from ...core.database import get_database_session
from ..oauth.entity import User
from ..oauth.models import UserInDB
from ..oauth.services import get_current_user
from ..persona.services import get_user_choices
from . import services
from .models.domain import CheckItem, ChecklistAnswer, CheckQuestion
from .models.responses import ChecklistAnswerResponse

router = APIRouter()


# @router.get(
#     path="/answers",
#     name="체크리스트 답변 리스트",
#     status_code=status.HTTP_200_OK,
#     response_model=ChecklistAnswerResponse,
# )
# async def get_checklist_answers(
#     current_user: UserInDB = Security(get_current_user),
#     session: Session = Depends(get_database_session),
# ) -> ChecklistAnswerResponse:
#     answers = (
#         session.query(ChecklistAnswer)
#         .join(User, User.uid == ChecklistAnswer.user_id)
#         .all()
#     )
#     return ChecklistAnswerResponse()


@router.get(
    path="",
    name="나의 체크리스트",
    status_code=status.HTTP_200_OK,
    response_model=List[CheckQuestion],
)
async def get_checklist(
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> List[CheckQuestion]:

    checklist = services.get_checklist(
        answers=get_user_choices(user_info=current_user, session=session),
        session=session,
    )
    return checklist
