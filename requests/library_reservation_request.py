from request_ABC import RequestABC
from libraryBooks.library_book import Book
from libraryUsers.library_user import LibraryUser


class ReservationRequest(RequestABC):
    def __init__(self, book: Book, user: LibraryUser, accepted: bool):
        self._book = book
        self._user = user
        self._accepted = accepted

    @property
    def book(self):
        return self._book

    @property
    def accepted(self):
        return self._accepted

    @property
    def user(self):
        return self._user
