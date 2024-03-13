from ..request_abc import RequestABC

class ReturnsRequest(RequestABC):
    
    def __init__(self, book_id: int, user_id: int):
        self._book_id = book_id
        self._user_id = user_id
        self._request_type = "returns"

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        self._book_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
