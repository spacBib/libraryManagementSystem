from ..request_abc import RequestABC
#from libraryBooks.library_book import LibraryBook

class ReservationRequest(RequestABC):
    
    def __init__(self, book: LibraryBook, user_id: int):
        self._book = book
        self._user_id = user_id
        self._request_type = "reservation"