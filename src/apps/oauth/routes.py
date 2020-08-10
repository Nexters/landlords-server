import requests
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette import status

from ...core.config import settings
from ...core.database import get_database_session
from .exceptions import InvalidToken
from .models.domain.google import GoogleUserInfo
from .models.domain.landlords import OAuthType, UserInfo
from .models.requests import CreateTokenRequest
from .models.responses import AppTokenResponse, JsonWebKeyResponse
from .services import create_access_token, get_jwk, sign_up_if_not_signed

router = APIRouter()


@router.get(
    path="/jwks.json", name="JWK 리스트", response_model=JsonWebKeyResponse
)
async def get_jwks() -> JsonWebKeyResponse:
    """ JWKS - [RFC 7571](https://tools.ietf.org/html/rfc7517) """
    public_key = get_jwk(key=settings.PUBLIC_KEY)
    return JsonWebKeyResponse(keys=[public_key])


GOOGLE_API = {
    "token_info": (
        "https://www.googleapis.com/oauth2/v1/tokeninfo"
        "?access_token={access_token}"
    ),
    "user_info": (
        "https://openidconnect.googleapis.com/v1/userinfo"
        "?access_token={access_token}"
    ),
}
token_router = APIRouter()


@token_router.post(
    path="",
    name="토큰 발급",
    description="oauth로 발급된 jwt",
    status_code=status.HTTP_201_CREATED,
    response_model=AppTokenResponse,
)
async def get_token(
    body: CreateTokenRequest, session: Session = Depends(get_database_session)
) -> AppTokenResponse:
    if body.oauth_type == OAuthType.Google:
        response = requests.get(
            GOOGLE_API["user_info"].format(access_token=body.access_token)
        )
        if response.status_code != status.HTTP_200_OK:
            raise InvalidToken
        google_user_info = GoogleUserInfo(**response.json())
        sign_up_if_not_signed(session, UserInfo(**google_user_info.dict()))
        app_token = create_access_token(google_user_info)
    return AppTokenResponse(token=app_token)
