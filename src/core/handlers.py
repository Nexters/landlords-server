"""
에러
"""
from typing import Union

from fastapi import status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from jwt import PyJWTError
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request
from starlette.responses import JSONResponse

from ..apps.rooms.exceptions import RoomNotFoundException

NotImplementedResponse = JSONResponse(
    {"errors": "not implemented"}, status_code=status.HTTP_501_NOT_IMPLEMENTED
)


async def database_exception_handler(
    _: Request, exc: SQLAlchemyError
) -> JSONResponse:
    response = NotImplementedResponse
    if isinstance(exc, RoomNotFoundException):
        response = JSONResponse(
            {"errors": str(exc)}, status_code=status.HTTP_404_NOT_FOUND
        )
    if isinstance(exc, SQLAlchemyError):
        if "Duplicate entry" in exc.args[0]:
            response = JSONResponse(
                {"errors": "이미 등록된 리소스 입니다"},
                status_code=status.HTTP_409_CONFLICT,
            )
        else:
            response = JSONResponse(
                {"errros": "관리자에게 문의 바랍니다"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    return response


async def http_exception_handler(
    _: Request, exc: HTTPException
) -> JSONResponse:
    """ http exception handling """
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)


async def validation_exception_handler(
    _: Request, exc: Union[RequestValidationError, ValidationError]
) -> JSONResponse:
    """ client request exception handling """
    return JSONResponse(
        {"errors": exc.errors()}, status_code=status.HTTP_400_BAD_REQUEST
    )


async def auth_exception_handler(_: Request, exc: PyJWTError) -> JSONResponse:
    return JSONResponse(
        {"error": str(exc)}, status_code=status.HTTP_401_UNAUTHORIZED
    )


validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": "{0}ValidationError".format(REF_PREFIX)},
    }
}
