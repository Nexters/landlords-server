from typing import Optional

from sqlalchemy.orm import Session

from ..oauth.models.domain.landlords import OAuthType
from .models.domain import UserInDB, UserInfo
from .models.entity import User


def sign_up_if_not_signed(
    session: Session, oauth_type: OAuthType, user_info: UserInfo
) -> None:
    if not find_by_email(session=session, email=user_info.email):
        sign_up(
            oauth_type=OAuthType.Google, session=session, user_info=user_info
        )


def find_by_email(session: Session, email: str) -> Optional[User]:
    user: Optional[User] = session.query(User).filter(
        User.email == email
    ).first()
    return user


def sign_up(
    session: Session, oauth_type: OAuthType, user_info: UserInfo
) -> UserInDB:
    user = User(
        oauth_type=oauth_type,
        disabled=False,
        **user_info.dict(exclude={"persona_answers"})
    )
    session.add(user)
    session.commit()
    return UserInDB.from_orm(user)
