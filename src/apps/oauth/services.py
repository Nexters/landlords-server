import time
from typing import Generator, Optional

from authlib.jose import jwk, jwt
from cryptography.hazmat.backends.openssl.rsa import _RSAPublicKey
from fastapi.param_functions import Depends
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session

from ...core.config import settings
from ...core.database import get_database_session
from ..users.models.domain import UserInDB, UserInfo
from ..users.models.entity import User
from .exceptions import UserNotFound
from .models.domain.landlords import JsonWebKey


def get_jwk(key: str) -> JsonWebKey:
    header = {"alg": "RS256", "kid": "landlords-1", "use": "sig"}
    jwk_dict = jwk.dumps(key, **header, kty="RSA")
    return JsonWebKey(**jwk_dict)


def get_public_key() -> Generator[_RSAPublicKey, None, None]:
    yield jwk.loads(get_jwk(settings.PUBLIC_KEY).dict())


def create_access_token(
    user_info: UserInfo,
    refresh_token: str = "",
    expiration: int = settings.ACCESS_TOKEN_EXPIRE_SECONDS,
) -> str:
    """ 액세스 토큰 생성 (JWT) """
    iat = int(time.time())
    exp = iat + expiration
    headers = {"alg": "RS256", "kid": "landlords-1"}
    jwt_body = user_info.dict()
    jwt_body.update({"iat": iat, "exp": exp})
    jwt_body["refresh_token"] = refresh_token
    token = jwt.encode(
        header=headers, payload=jwt_body, key=settings.PRIVATE_KEY
    )
    return str(token, "utf-8")


def decode_token(token: str, public_key: _RSAPublicKey) -> UserInfo:
    payload = jwt.decode(token, public_key)
    token_data = UserInfo(**payload)
    return token_data


AUTH_HEADER = APIKeyHeader(name="Authorization")


async def get_current_user(
    token: str = Depends(AUTH_HEADER),
    session: Session = Depends(get_database_session),
    public_key: _RSAPublicKey = Depends(get_public_key),
) -> UserInDB:
    user_info = decode_token(token, public_key)
    user: Optional[User] = session.query(User).filter(
        User.email == user_info.email
    ).first()
    if not user or user.disabled:
        raise UserNotFound

    return UserInDB(
        uid=user.uid,
        oauth_type=user.oauth_type,
        disabled=user.disabled,
        **user_info.dict(),
    )
