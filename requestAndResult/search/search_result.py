from ..result_abc import ResultABC
from libraryBooks.library_book import LibraryBook

class SearchResult(ResultABC):
    
    def __init__(self, search_str: str, user_id: int, results: list['LibraryBook']):
        self._search_string = search_str
        self._user_id = user_id
        self._results = results

    @property
    def search_string(self):
        return self._search_string

    @search_string.setter
    def search_string(self, value):
        self._search_string = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        self._results = value

    
    
    def print_result(self):
        print("\n")
        print(self.results)

            