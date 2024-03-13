from ..result_abc import ResultABC
from libraryBooks.library_book import LibraryBook

class ReservationResult(ResultABC):
    
    def __init__(self, search_str: str, user_id: int, results: list['LibraryBook']):
        self._search_string = search_str
        self._user_id = user_id
        self._results = results