import httpx
import requests
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette import status

from ...core.config import oauth_settings, settings
from ...core.database import get_database_session
from ..users.exceptions import InvalidToken
from ..users.models.domain import UserInfo
from ..users.services import sign_up_if_not_signed
from ..users.services.kakao import get_user_profile
from .models.domain.google import GoogleUserInfo
from .models.domain.landlords import OAuthType
from .models.requests import CreateTokenRequest
from .models.responses import (
    AppTokenResponse,
    JsonWebKeyResponse,
    KakaoAuthResponse,
)
from .services import create_access_token, get_jwk

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
        sign_up_if_not_signed(
            session=session,
            oauth_type=body.oauth_type,
            user_info=UserInfo(**google_user_info.dict()),
        )
        app_token = create_access_token(google_user_info)
    elif body.oauth_type == OAuthType.Kakao:
        kakao_response = httpx.post(
            "https://kauth.kakao.com/oauth/token",
            headers={
                "content-type": (
                    "application/x-www-form-urlencoded;charset=utf-8"
                )
            },
            data={
                "grant_type": "refresh_token",
                "client_id": oauth_settings.KAKAO_REST_API_KEY,
                "refresh_token": body.access_token,
                "client_secret": oauth_settings.KAKAO_CLIENT_SECRET,
            },
        )
        if kakao_response.status_code != status.HTTP_200_OK:
            raise InvalidToken
        kakao_auth_response = KakaoAuthResponse(**kakao_response.json())
        kakao_auth_info = await get_user_profile(
            access_token=kakao_auth_response.access_token
        )
        user_info = UserInfo(
            sub="",
            email="",
            name=kakao_auth_info.properties.nickname,
            picture=kakao_auth_info.properties.profile_image,
        )
        sign_up_if_not_signed(
            session=session, oauth_type=OAuthType.Kakao, user_info=user_info
        )
        app_token = create_access_token(
            user_info, refresh_token=kakao_auth_response.refresh_token
        )
    else:
        raise HTTPException(status_code=400)
    return AppTokenResponse(token=app_token)
