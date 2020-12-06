# pylint: disable=no-self-argument
from typing import Any, Dict, List, Optional, Union

from fastapi.logger import logger
from pydantic import BaseSettings, HttpUrl, ValidationError, validator


class OAuthSettings(BaseSettings):
    KAKAO_REST_API_KEY: str = ""
    KAKAO_CLIENT_SECRET: str = ""
    KAKAO_AUTH_REDIRECT_URI: str = ""


class SQLAlchemySettings(BaseSettings):
    MYSQL_USER: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_ROOT_PASSWORD: str = ""
    MYSQL_HOST: str = ""
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = ""
    MYSQL_QUERY: Optional[Dict[str, Any]] = None

    SQLALCHEMY_POOL_SIZE: int = 5
    SQLALCHEMY_POOL_TIMEOUT: int = 10
    SQLALCHEMY_POOL_RECYCLE: int = 3600
    SQLALCHEMY_ECHO: bool = False

    class Config:
        """ setting의 부가 설정 """

        case_sensitive = True


class Settings(BaseSettings):
    """
    application 설정 (환경변수 최우선)
    """

    API_VERSION_PREFIX: str = "/v1"
    PRIVATE_KEY: str = ""
    PUBLIC_KEY: str = ""
    JWT_ALGORITHM: str = "RS256"
    SECRET_KEY: str = ""
    WEB_URI: HttpUrl = "https://checkhaebang.com"  # type: ignore
    CORS_ALLOWS: List[HttpUrl] = []

    ACCESS_TOKEN_EXPIRE_SECONDS: int = 86400 * 7

    @validator("CORS_ALLOWS", pre=True)
    def __set_cors_allows(cls, v: Union[str, List[str]]) -> List[str]:  # noqa
        result = v
        if isinstance(v, str) and not v.startswith("["):
            result = [i.strip() for i in v.split(",")]
        elif isinstance(v, List):
            result = v
        else:
            raise ValueError(v)
        return result

    @validator("PRIVATE_KEY", pre=True)
    def __set_private_key(cls, value: str) -> str:  # noqa
        return value.replace("\\n", "\n")

    @validator("PUBLIC_KEY", pre=True)
    def __set_public_key(cls, value: str) -> str:  # noqa
        return value.replace("\\n", "\n")

    class Config:
        """ setting의 부가 설정 """

        case_sensitive = True


try:
    settings = Settings()
    sqlalchemy_settings = SQLAlchemySettings()
    oauth_settings = OAuthSettings()
except ValidationError as err:
    logger.error(err)
