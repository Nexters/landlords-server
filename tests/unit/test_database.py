from src.core.database import get_database_session


def test_session() -> None:
    """
    https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-dependency
    """
    session_generator = get_database_session()
    session = next(session_generator)
    assert session
