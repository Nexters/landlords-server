from pydantic import BaseModel

from .domain.landlords import OAuthType


class CreateTokenRequest(BaseModel):
    oauth_type: OAuthType
    access_token: str
