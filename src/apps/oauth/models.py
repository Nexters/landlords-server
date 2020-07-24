from pydantic import BaseModel


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
    picture: str
    name: str
    given_name: str
    family_name: str
