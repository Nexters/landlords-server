from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL as SQLAlchemyURL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from .config import sqlalchemy_settings

engine = create_engine(
    SQLAlchemyURL(
        drivername="mysql+pymysql",
        username=sqlalchemy_settings.MYSQL_USER,
        password=sqlalchemy_settings.MYSQL_PASSWORD,
        host=sqlalchemy_settings.MYSQL_HOST,
        port=sqlalchemy_settings.MYSQL_PORT,
        database=sqlalchemy_settings.MYSQL_DATABASE,
        query=sqlalchemy_settings.MYSQL_QUERY,
    ),
    pool_size=sqlalchemy_settings.SQLALCHEMY_POOL_SIZE,
    pool_recycle=sqlalchemy_settings.SQLALCHEMY_POOL_RECYCLE,
    pool_timeout=sqlalchemy_settings.SQLALCHEMY_POOL_TIMEOUT,
    echo=sqlalchemy_settings.SQLALCHEMY_ECHO,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_database_session() -> Generator[Session, None, None]:
    """ sqlalchemy Session generator """
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
