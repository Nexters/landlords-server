from enum import Enum

from pydantic import BaseModel


class TokenType(str, Enum):
    """ 토큰 타입 """

    BEARER = "bearer"


class TokenData(BaseModel):
    """ 토큰 정보 """

    id: int = 0
    email: str = ""
    fullname: str = ""
    profile: str = ""
