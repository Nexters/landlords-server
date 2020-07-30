from typing import List, Optional

from pydantic import BaseModel, Field

from .entity import OAuthType


class GoogleUserInfo(BaseModel):
    iss: str
    azp: str
    aud: str
    sub: str
    email_verified: bool
    at_hash: str
    nonce: str

    email: str
    name: str
    picture: str
    given_name: str
    family_name: str
    iat: int
    exp: int
    locale: str


class UserInfo(BaseModel):
    email: str
    name: str
    given_name: str
    family_name: str
    picture: str


class UserInDB(UserInfo):
    uid: int
    oauth_type: OAuthType
    at_hash: str
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


class JsonWebKeyResponse(BaseModel):
    keys: List[JsonWebKey]
