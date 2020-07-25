# from unittest.mock import Mock

# from src.apps.oauth.models import UserInfo
# from src.apps.persona.models.domain import QuestionCategory
# from src.apps.persona.models.entity import ChoiceItem, QuestionAnswer
# from src.apps.persona.models.responses import PersonaQuestionsResponse
# from src.apps.persona.services import get_user_choices
# from src.core.database import SessionLocal


# def test_get_persona() -> None:
#     session = SessionLocal()
#     answers = get_user_choices(
#         user_info=UserInfo(
#             email="piercecaelum@gmail.com",
#             picture="",
#             name="",
#             given_name="",
#             family_name="",
#         ),
#         session=session,
#     )
#     assert answers
