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
from ..rooms.models.entity import Room
from . import services
from .models.domain import CheckAnswer as CheckAnswerDto
from .models.domain import CheckItem as CheckItemDto
from .models.domain import Checklist
from .models.domain import CheckQuestion as CheckQuestionDto
from .models.entity import CheckAnswer, CheckItem, CheckQuestion

router = APIRouter()


@router.get(
    path="",
    name="나의 체크리스트",
    status_code=status.HTTP_200_OK,
    response_model=Checklist,
)
async def get_checklist(
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> Checklist:

    checklist: Checklist = services.get_checklist(
        answers=get_user_choices(user_info=current_user, session=session),
        session=session,
    )

    return Checklist(
        questions=[CheckQuestionDto.from_orm(check) for check in checklist]
    )
