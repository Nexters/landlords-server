from http import HTTPStatus

from fastapi.exceptions import HTTPException

UserNotFound = HTTPException(
    status_code=HTTPStatus.NOT_FOUND, detail="해당하는 유저가 없습니다"
)

InvalidToken = HTTPException(
    status_code=HTTPStatus.UNAUTHORIZED, detail="유효하지 않은 토큰입니다"
)
