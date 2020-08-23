from http import HTTPStatus
from http.client import HTTPConnection, HTTPSConnection
from urllib.parse import ParseResult, urlparse

from fastapi.param_functions import Query
from fastapi.routing import APIRouter
from pydantic import BaseModel, HttpUrl
from starlette import status

proxy_redirect = APIRouter()


class ProxyRedirectResponse(BaseModel):
    url: HttpUrl


@proxy_redirect.get(
    path="",
    status_code=status.HTTP_200_OK,
    response_model=ProxyRedirectResponse,
    description="proxy redirect",
)
async def proxy_redirect_url(
    url: HttpUrl = Query(...)
) -> ProxyRedirectResponse:
    result = proxy_redirect_request(str(url))
    return ProxyRedirectResponse(url=result)  # type: ignore


def proxy_redirect_request(url: str) -> str:
    result: ParseResult = urlparse(url=url)
    conn = (
        HTTPSConnection(host=result.netloc)
        if result.scheme == "https"
        else HTTPConnection(host=result.netloc)
    )
    conn.request(method="GET", url=result.path)
    response = conn.getresponse()

    return (
        response.headers.get("Location")
        if response.status == HTTPStatus.FOUND
        else result.geturl()
    )
