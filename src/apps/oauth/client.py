from http import HTTPStatus

import httpx
from authlib.common.errors import AuthlibBaseError
from authlib.integrations.starlette_client import OAuth
from fastapi.applications import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse

from ...core.config import oauth_settings, settings
from ...core.database import get_database_session
from ...core.handlers import set_exception_handlers
from ..users.models.domain import UserInfo
from ..users.services import sign_up_if_not_signed
from ..users.services.kakao import get_user_profile
from .models.domain.google import GoogleAuthInfo
from .models.domain.landlords import OAuthType
from .models.responses import KakaoAuthResponse
from .services import create_access_token

config = Config("google.env")
oauth = OAuth(config)
oauth.register(
    name="google",
    server_metadata_url=(
        "https://accounts.google.com/.well-known/openid-configuration"
    ),
    client_kwargs={"scope": "openid email profile"},
)


oauth_client = FastAPI()
oauth_client.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
set_exception_handlers(oauth_client)


@oauth_client.exception_handler(AuthlibBaseError)
async def handle_auth_error(
    request: Request, exc: AuthlibBaseError
) -> JSONResponse:
    return JSONResponse(
        content={"message": exc.description},
        status_code=HTTPStatus.UNAUTHORIZED,
    )


@oauth_client.route("/google")
async def google_login(request: Request):  # type: ignore
    redirect_uri = request.url_for("oauth:sign_in")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@oauth_client.get("/sign_in")
async def sign_in(
    request: Request, session: Session = Depends(get_database_session)
) -> RedirectResponse:
    google_auth_info = GoogleAuthInfo.parse_obj(
        await oauth.google.parse_id_token(
            request, await oauth.google.authorize_access_token(request)
        )
    )
    sign_up_if_not_signed(
        session=session,
        oauth_type=OAuthType.Google,
        user_info=UserInfo(**google_auth_info.dict(by_alias=True)),
    )
    app_token = create_access_token(google_auth_info)
    response = RedirectResponse(url=settings.WEB_URI)
    response.set_cookie(
        key="token", value=app_token, domain=settings.WEB_URI.host
    )
    return response


@oauth_client.get("/kakao", response_class=RedirectResponse)
def kakao_login(request: Request):  # type: ignore
    """ 카카오 oauth 서버로 부터 인가코드를 받아서 kakao access token을 발급받는 부분 """
    url = (
        "https://kauth.kakao.com/oauth/authorize"
        f"?client_id={oauth_settings.KAKAO_REST_API_KEY}"
        f"&redirect_uri={oauth_settings.KAKAO_AUTH_REDIRECT_URI}"
        "&response_type=code"
    )
    response = httpx.get(url)
    return RedirectResponse(response.history[0].headers["location"])


@oauth_client.get("/kakao/sign_in")
async def kakao_sign_in(
    request: Request, session: Session = Depends(get_database_session)
) -> RedirectResponse:
    response = httpx.post(
        "https://kauth.kakao.com/oauth/token",
        headers={
            "content-type": "application/x-www-form-urlencoded;charset=utf-8"
        },
        data={
            "grant_type": "authorization_code",
            "client_id": oauth_settings.KAKAO_REST_API_KEY,
            "redirect_uri": oauth_settings.KAKAO_AUTH_REDIRECT_URI,
            "code": request.query_params["code"],
            "client_secret": oauth_settings.KAKAO_CLIENT_SECRET,
        },
    )
    kakao_auth_response = KakaoAuthResponse(**response.json())
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
    redirect = RedirectResponse(url=settings.WEB_URI)
    redirect.set_cookie(
        key="token", value=app_token, domain=settings.WEB_URI.host
    )
    return redirect
