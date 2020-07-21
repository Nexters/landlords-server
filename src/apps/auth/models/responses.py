from typing import List, Optional

from pydantic import BaseModel, Field

from .domain.tokens import TokenType


class TokenResponse(BaseModel):
    """ 토큰 결과 """

    access_token: str
    token_type: TokenType


class UserResponse(BaseModel):

    id: int
    email: Optional[str] = ""
    full_name: Optional[str] = ""
    profile: Optional[str] = ""
    disabled: Optional[bool] = False

    class Config:
        orm_mode = True
