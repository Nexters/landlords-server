from datetime import datetime
from typing import List

from pydantic import BaseModel, Extra

from .domain.kakao import KakaoAccount, Properties
from .domain.landlords import JsonWebKey


class JsonWebKeyResponse(BaseModel):
    keys: List[JsonWebKey]


class AppTokenResponse(BaseModel):
    token: str


class KakaoAuthResponse(BaseModel):
    """ 카카오 인증 response
        https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#request-token
    """

    access_token: str
    token_type: str
    refresh_token: str
    expires_in: int
    scope: str
    refresh_token_expires_in: int


class KakaoUserMeResponse(BaseModel):
    """ 카카오 사용자 정보 가져오기
        https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#req-user-info
    """

    id: int
    connected_at: datetime
    properties: Properties
    kakao_account: KakaoAccount

    class Config:
        extra = Extra.allow
