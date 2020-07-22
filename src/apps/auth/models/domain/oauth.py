from pydantic import BaseModel


class GoogleOAuthInfo(BaseModel):
    id: str
    email: str
    verifiedemail: bool
    name: str
    givenname: str
    familyname: str
    picture: str
    locale: str
