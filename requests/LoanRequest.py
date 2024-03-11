from RequestABC import RequestABC
from libraryBooks.book import Book


class LoanRequest(RequestABC):
    
    def __init__(self, book: Book):
        self._book = book
        
    @property
    def book(self):
        return self._book