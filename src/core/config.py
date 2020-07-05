# pylint: disable=no-self-argument
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    application 설정 (환경변수 최우선)
    """

    API_VERSION_PREFIX: str = "/api/v1"

    class Config:
        """ setting의 부가 설정 """

        case_sensitive = True


settings = Settings()
