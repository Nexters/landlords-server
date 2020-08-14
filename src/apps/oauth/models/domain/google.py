"""
https://accounts.google.com/.well-known/openid-configuration
"""

from pydantic import BaseModel, Field

from ....users.models.domain import UserInfo


class GoogleUserInfo(UserInfo):
    family_name: str = Field(..., description="성")
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
