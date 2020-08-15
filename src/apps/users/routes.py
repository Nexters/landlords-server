from fastapi.param_functions import Depends, Security
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette import status

from ...core.database import get_database_session
from ..oauth.services import get_current_user
from ..persona.services import get_user_choices
from .models.domain import UserInDB
from .models.responses import UserInfoResponse

router = APIRouter()


@router.get(
    path="",
    name="유저 정보 불러오기",
    status_code=status.HTTP_200_OK,
    response_model=UserInfoResponse,
)
async def get_users(
    current_user: UserInDB = Security(get_current_user),
    session: Session = Depends(get_database_session),
) -> UserInfoResponse:
    response = UserInfoResponse(**current_user.dict())
    response.persona_answers = get_user_choices(
        session=session, user_info=current_user
    )
    return response
