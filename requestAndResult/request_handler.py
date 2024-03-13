from request_abc import RequestABC
from libraryDatabase.info_getter import InfoGetter
from libraryDatabase.database_connector import ConnectToDatabase

class RequestHandler(object):
    
    def __init__(self) -> None:
        self._info_getter = InfoGetter()
    
    
    def handle_request(self, request: RequestABC):
        match request._request_type:
            case "search":
                result = self._search_request(request)
            case "loan":
                result = self._loan_request(request)
            case "reservation":
                result = self._reservation_request(request)
            case "return":
                result = self._return_request(request)
    
    def _search_request(self, request: RequestABC):
        pass
    
    def _loan_request(self, request: RequestABC):
        pass
    
    def _reservation_request(self, request: RequestABC):
        pass
    
    def _return_request(self, request: RequestABC):
        pass
    
    