"""
https://accounts.google.com/.well-known/openid-configuration
"""

from typing import Optional

from pydantic import BaseModel, Field

from ....users.models.domain import UserInfo


class GoogleUserInfo(UserInfo):
    """ 구글 유저 정보
    family_name이 없는 나라도 있음
    """

    family_name: Optional[str] = Field(default="", description="성")
    given_name: str = Field(..., description="이름")
    email_verified: bool = Field(..., description="이메일 인증 여부")
    locale: str = Field(..., description="국가")


class GoogleAuthInfo(GoogleUserInfo):
    iss: str
    azp: str
    aud: str
    at_hash: str
    nonce: str
    iat: int
    exp: int

    class Config:
        allow_population_by_field_name = True


class GoogleAccessToken(BaseModel):
    issued_to: str
    audience: str
    user_id: str
    scope: str
    expires_in: int
    email: str
    verified_email: bool
    access_type: str


class GoogleAPIError(BaseModel):
    error: str
    error_description: str
