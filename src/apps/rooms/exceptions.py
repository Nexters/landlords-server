from ...core.exceptions import CrawlingException, RepositoryException


class NoneTypeError(CrawlingException):
    """ 값이 없습니다 """


class RoomNotFoundException(RepositoryException):
    """ 방 매물 정보 없음 """
