from .loan_request import LoanRequest
from .loan_result import LoanResult
from ..factory_abc import ResultRequestFactoryABC
from libraryBooks.library_book import LibraryBook
from libraryBooks.library_book_factory import BookFactory

class LoanFactory(ResultRequestFactoryABC):
    
    def create_request(self, book_id: int, user_id:int) -> LoanRequest:
        return LoanRequest(book_id, user_id)
    
    def create_result(self, request: LoanRequest, book_info: dict, success: bool) -> LoanResult:
        book = self._make_book(book_info)
        user_id = request._user_id
        return LoanResult(book, user_id, success)
    
    def _make_book(self, info: dict) -> LibraryBook:
        factory = BookFactory()
        return factory.create_from_dict(info)