from ...core.exceptions import CrawlingException, RepositoryException


class NoneTypeError(CrawlingException):
    """ 값이 없습니다 """


class RoomNotFoundException(RepositoryException):
    """ 방 매물 정보 없음 """


class AnswerNotFoundException(RepositoryException):
    """체크리스트에 응답한 목록이 없습니다. """
