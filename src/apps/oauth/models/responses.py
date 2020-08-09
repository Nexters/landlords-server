from typing import List

from pydantic import BaseModel

from .domain.landlords import JsonWebKey


class JsonWebKeyResponse(BaseModel):
    keys: List[JsonWebKey]


class AppTokenResponse(BaseModel):
    token: str
