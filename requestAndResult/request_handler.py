from requestAndResult.request_abc import RequestABC
from libraryDatabase.info_getter import InfoGetter
from libraryDatabase.database_connector import ConnectToDatabase
from requestAndResult.search.search_request import SearchRequest
from requestAndResult.search.search_result import SearchResult
from requestAndResult.reservation.reservation_request import ReservationRequest
from requestAndResult.reservation.reservation_result import ReservationResult
#from search.search_factory import SearchFactory
from requestAndResult.factory_finder import FactoryFinder
import requestAndResult.result_abc
class RequestHandler(object):
    
    def __init__(self) -> None:
        db_connecter = ConnectToDatabase()
        sql_connection = db_connecter.connect_to_database("library_management_system")
        self._info_getter = InfoGetter(sql_connection)
    
    
    def handle_request(self, request: RequestABC) -> requestAndResult.result_abc.ResultABC:
        match request.request_type:
            case "search":
                return self._search_request(request)
            case "loan":
                result = self._loan_request(request)
            case "reservation":
                return self._reservation_request(request)
            case "return":
                result = self._return_request(request)
    
    def _search_request(self, request: SearchRequest) -> SearchResult:
        result_list = self._info_getter.search_title(request.search_str)
        factory = FactoryFinder().get_concrete_factory("search")
        return factory.create_result(request, result_list)
    
    def _loan_request(self, request: RequestABC):
        pass
    
    def _reservation_request(self, request: ReservationRequest) -> ReservationResult:
        success = self._info_getter.reserve_book(request._book_id, request._user_id)
        book_info = self._info_getter.search_book_id(request._book_id)
        factory = FactoryFinder().get_concrete_factory(request._request_type)
        return factory.create_result(request, book_info, success)
    
    def _return_request(self, request: RequestABC):
        pass
    
    