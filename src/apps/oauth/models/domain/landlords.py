from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class OAuthType(str, Enum):
    Google = "Google"


class UserInfo(BaseModel):
    sub: str = Field(..., description="구글 jwt sub")
    email: str = Field(..., description="이메일")
    name: str = Field(..., description="전체 이름")
    picture: str = Field(..., description="프로필 이미지")


class UserInDB(UserInfo):
    uid: int
    oauth_type: OAuthType
    sub: str
    disabled: bool

    class Config:
        orm_mode = True


class JsonWebKey(BaseModel):
    """ JWKS - [RFC 7571](https://tools.ietf.org/html/rfc7517) """

    kty: str = Field(..., description="사용되는 값")
    n: str = Field(..., description="RSA modulus")
    e: str = Field(..., description="RSA public exponent")
    kid: Optional[str] = Field(
        default="ims-1",
        description="jwt의 encode시 사용된 key의 고유 식별자 (for key rolling)",
    )
    alg: Optional[str] = Field(default="RSA256", description="사용된 알고리즘")
    use: Optional[str] = Field(
        default="sig", description="용도 (sig: signature, verify 검증)"
    )
