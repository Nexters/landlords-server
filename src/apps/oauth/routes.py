from fastapi.routing import APIRouter

from ...core.config import settings
from .models import JsonWebKeyResponse
from .services import get_jwk

router = APIRouter()


@router.get(
    path="/jwks.json", name="JWK 리스트", response_model=JsonWebKeyResponse
)
async def get_jwks() -> JsonWebKeyResponse:
    """ JWKS - [RFC 7571](https://tools.ietf.org/html/rfc7517) """
    public_key = get_jwk(key=settings.PUBLIC_KEY)
    return JsonWebKeyResponse(keys=[public_key])
