from .reservation_request import ReservationRequest
from .reservation_result import ReservationResult
from ..factory_abc import ResultRequestFactoryABC
from libraryBooks.library_book import LibraryBook
from libraryBooks.library_book_factory import BookFactory

class ReservationFactory(ResultRequestFactoryABC):
    
    def create_request(self, book_id: int, user_id:int) -> ReservationRequest:
        return ReservationRequest(book_id, user_id)
    
    def create_result(self, request: ReservationRequest, book_info: dict, success: bool) -> ReservationResult:
        book = self._make_book(book_info)
        user_id = request._user_id
        return ReservationResult(book, user_id, success)
    
    def _make_book(self, info: dict) -> LibraryBook:
        factory = BookFactory()
        return factory.create_from_dict(info)