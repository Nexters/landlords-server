from typing import Optional

from fastapi import status
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from ....core.database import get_database_session
from ...auth.services import create_access_token
from ..models.domain.tokens import TokenType
from ..models.domain.user import UserInDB
from ..models.entity import User
from ..models.responses import TokenResponse

router = APIRouter()


@router.get(
    path="",
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse,
    description="토큰 발급",
)
async def token(
    email: str,
    name: str,
    picture: str,
    session: Session = Depends(get_database_session),
) -> TokenResponse:
    user: Optional[User] = session.query(User).filter(
        User.email == email
    ).first()
    if not user:
        user = User(
            email=email, full_name=name, profile=picture, disabled=False
        )
        session.add(user)
        session.commit()
        session.refresh(user)

    return TokenResponse(
        access_token=create_access_token(UserInDB.from_orm(user)),
        token_type=TokenType.BEARER,
    )
