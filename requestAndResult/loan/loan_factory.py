from ..factory_abc import ResultRequestFactoryABC
from libraryBooks.library_book import LibraryBook
class LoanFactory(ResultRequestFactoryABC):
    
    #@staticmethod
    def create_request(self, book: LibraryBook, user_id: int):
        pass
    
    
    #@staticmethod
    def create_result():
        pass