from .search_request import SearchRequest
from .search_result import SearchResult
from ..factory_abc import ResultRequestFactoryABC
from libraryBooks.library_book import LibraryBook
from libraryBooks.library_book_factory import BookFactory
class SearchFactory(ResultRequestFactoryABC):
    
    def create_request(self, search_str: str, user_id: int) -> SearchRequest:
        return SearchRequest(search_str, user_id)

    def create_result(self, request: SearchRequest, search_results: list['dict']) -> SearchResult:
        books = self._make_books(search_results)
        sr = SearchResult(
            search_str = request.search_str,
            user_id = request.user_id,
            results = books
        )
        return sr
    
    def _make_books(self, info_list: list['dict']) -> list['LibraryBook']:
        factory = BookFactory()
        book_list = list()
        for dict in info_list:
            book_list.append(
                factory.create_from_dict(dict)
            )
        return book_list