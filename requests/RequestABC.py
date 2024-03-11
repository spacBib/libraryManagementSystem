import abc
from libraryBooks.book import Book


class RequestABC(abc.ABC):
    
    @property
    @abc.abstractmethod
    def book(self):
        pass
    

    
    
        
    
    
    