from request_abc import RequestABC

class SearchRequest(RequestABC):
    
    def __init__(self, search_str: str, user_id: int):
        self._search_str = search_str
        self._user_id = user_id

    @property
    def search_str(self):
        return self._search_str

    @search_str.setter
    def search_str(self, value):
        self._search_str = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

        
    
        
    