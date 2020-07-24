import time

import jwt
from fastapi.param_functions import Depends
from fastapi.security.api_key import APIKeyHeader

from ...core.config import settings
from .models import GoogleUserInfo, UserInfo


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


async def get_current_user(token: str = Depends(AUTH_HEADER)) -> UserInfo:
    return decode_token(token)
