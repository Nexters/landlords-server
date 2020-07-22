class UserNotFoundException(Exception):
    """ 해당하는 User를 찾지 못했습니다 """


class AuthError(Exception):
    def __init__(self, error: str, status_code: int) -> None:
        self.error = error
        self.status_code = status_code
