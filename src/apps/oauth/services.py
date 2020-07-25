import time
from http import HTTPStatus
from typing import Optional

import jwt
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session

from ...core.config import settings
from ...core.database import get_database_session
from .entity import User
from .models import GoogleUserInfo, UserInDB, UserInfo


def create_access_token(
    google_user_info: GoogleUserInfo,
    expiration: int = settings.ACCESS_TOKEN_EXPIRE_SECONDS,
) -> str:
    """ 액세스 토큰 생성 (JWT) """
    iat = int(time.time())
    exp = iat + expiration
    jwt_body = google_user_info.dict(
        exclude={
            "iss",
            "azp",
            "aud",
            "sub",
            "email_verified",
            "at_hash",
            "nonce",
        }
    )
    jwt_body.update({"iat": iat, "exp": exp})
    token = jwt.encode(jwt_body, settings.PRIVATE_KEY, settings.JWT_ALGORITHM)
    return str(token, "utf-8")


def decode_token(token: str) -> UserInfo:
    payload = jwt.decode(
        token, settings.PUBLIC_KEY, algorithms=settings.JWT_ALGORITHM
    )
    token_data = UserInfo(**payload)
    return token_data


AUTH_HEADER = APIKeyHeader(name="Authorization")


async def get_current_user(
    token: str = Depends(AUTH_HEADER),
    session: Session = Depends(get_database_session),
) -> UserInDB:
    user_info = decode_token(token)
    user: Optional[User] = session.query(User).filter(
        User.email == user_info.email
    ).first()
    if not user or user.disabled:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="해당하는 유저가 없습니다"
        )

    return UserInDB(
        uid=user.uid,
        oauth_type=user.oauth_type,
        at_hash=user.at_hash,
        disabled=user.disabled,
        **user_info.dict()
    )
