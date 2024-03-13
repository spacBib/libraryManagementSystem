from search_request import SearchRequest
from search_result import SearchResult
from libraryUsers.library_user import LibraryUser
from factory_abc import ResultRequestFactoryABC

class SearchFactory(ResultRequestFactoryABC):
    
    #@staticmethod
    def create_request(search_str: str, user_id: int) -> SearchRequest:
        return SearchRequest(search_str, user_id)
    
    #@staticmethod
    def create_result(request: SearchRequest, search_results: list) -> SearchResult:
        sr = SearchResult(
            search_str = request.search_str,
            user_id = request.user_id,
            results = search_results
        )
        return sr