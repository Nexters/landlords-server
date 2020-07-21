import os
import time
from http import HTTPStatus
from typing import Any, Dict, Iterable, List, Optional

import jwt
import requests
from fastapi.param_functions import Depends, Security
from fastapi.security.oauth2 import (
    OAuth2AuthorizationCodeBearer,
    SecurityScopes,
)

from ...core.config import settings
from .models.domain.tokens import TokenData
from .models.domain.user import UserInDB

AUTH0_DOMAIN = "https://accounts.google.com/o/oauth2/v2/auth"
AUTHORIZATION_URL = os.environ.get(
    "AUTHORIZATION_URL", "https://accounts.google.com/o/oauth2/auth"
)
TOKEN_URL = os.environ.get("TOKEN_URL", "https://oauth2.googleapis.com/token")
JWKS_URI = os.environ.get(
    "JWKS_URI", "https://www.googleapis.com/oauth2/v3/certs"
)
ALGORITHMS = ["RS256"]
USER_INFO_URL = (
    "https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}"
)

auth0_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=AUTHORIZATION_URL,
    tokenUrl=TOKEN_URL,
    scopes={"openid": "openid", "email": "email", "profile": "profile"},
)


def create_access_token(
    user: UserInDB, expiration: int = settings.ACCESS_TOKEN_EXPIRE_SECONDS
) -> str:
    """ 액세스 토큰 생성 (JWT) """
    iat = int(time.time())
    exp = iat + expiration
    jwt_body = {
        "id": user.id,
        "email": user.email,
        "fullname": user.full_name,
        "profile": user.profile,
        "iat": iat,
        "exp": exp,
    }
    token = jwt.encode(
        jwt_body, settings.PRIVATE_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return str(token, "utf-8")


async def decode_token(token: str) -> Optional[TokenData]:
    token_data: Optional[TokenData] = None
    try:
        payload = jwt.decode(
            token, settings.PUBLIC_KEY, algorithms=settings.JWT_ALGORITHM
        )
        id = payload.get("id", None)
        email = payload.get("email", None)
        fullname = payload.get("fullname", None)
        profile = payload.get("profile", None)
        token_data = TokenData(
            id=id, email=email, fullname=fullname, profile=profile
        )
    except jwt.PyJWTError as err:
        raise err
    finally:
        return token_data


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Security(auth0_scheme)
) -> Any:
    response = requests.get(USER_INFO_URL.format(access_token=token))
    if response.status_code == HTTPStatus.OK:
        return response.json()
