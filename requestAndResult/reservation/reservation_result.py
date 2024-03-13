from ..result_abc import ResultABC
from libraryBooks.library_book import LibraryBook

class ReservationResult(ResultABC):
    
    def __init__(self, book: LibraryBook, user_id: int, success: bool):
        self._book = book
        self._user_id = user_id
        self._success = success

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        self._book = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
