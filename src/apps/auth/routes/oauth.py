import token
from typing import Dict

from fastapi.param_functions import Security
from fastapi.routing import APIRouter
from starlette.responses import RedirectResponse

from ..models.domain.oauth import GoogleOAuthInfo
from ..services import get_current_user

router = APIRouter()


@router.get("/google/private")
async def google_private(
    info: GoogleOAuthInfo = Security(get_current_user)
) -> RedirectResponse:
    return RedirectResponse(
        "/token"
        "?email={info['email']}"
        "&name={info['name']}"
        "&picture={info['picture']}"
    )


@router.get("/google/private-with-scopes")
async def google_privateScopes(
    info: GoogleOAuthInfo = Security(get_current_user, scopes=["openid"])
) -> Dict[str, str]:
    return {"message": "You're authorized with scopes!"}
