from .returns_request import ReturnsRequest
from .returns_result import ReturnsResult
from ..factory_abc import ResultRequestFactoryABC
from libraryBooks.library_book import LibraryBook
from libraryBooks.library_book_factory import BookFactory

class ReturnsFactory(ResultRequestFactoryABC):
    
    def create_request(self, book_id: int, user_id:int) -> ReturnsRequest:
        return ReturnsRequest(book_id, user_id)
    
    def create_result(self, request: ReturnsRequest, book_info: dict, success: bool) -> ReturnsResult:
        book = self._make_book(book_info)
        user_id = request._user_id
        return ReturnsResult(book, user_id, success)
    
    def _make_book(self, info: dict) -> LibraryBook:
        factory = BookFactory()
        return factory.create_from_dict(info)