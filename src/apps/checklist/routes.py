from fastapi import status
from fastapi.param_functions import Depends, Security
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from ...core.database import get_database_session
from ..oauth.services import get_current_user
from ..users.models.domain import UserInDB
from . import services
from .models.domain import StatusCategory
from .models.responses import ChecklistResponse

router = APIRouter()


@router.get(
    path="",
    name="나의 체크리스트",
    status_code=status.HTTP_200_OK,
    response_model=ChecklistResponse,
)
async def get_checklist(
    status: StatusCategory,
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> ChecklistResponse:

    return ChecklistResponse(
        questions=services.get_checklist(
            user_info=current_user, session=session, status=status
        )
    )
