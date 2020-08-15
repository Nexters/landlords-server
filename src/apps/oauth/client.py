from http import HTTPStatus

from authlib.common.errors import AuthlibBaseError
from authlib.integrations.starlette_client import OAuth
from fastapi.applications import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse

from ...core.config import settings
from ...core.database import get_database_session
from ..users.models.domain import UserInfo
from ..users.services import sign_up_if_not_signed
from .models.domain.google import GoogleAuthInfo
from .models.domain.landlords import OAuthType
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
        user_info=UserInfo(**google_auth_info.dict()),
    )
    app_token = create_access_token(google_auth_info)
    response = RedirectResponse(url=settings.WEB_URI)
    response.set_cookie(
        key="token", value=app_token, domain=settings.WEB_URI.host
    )
    return response
