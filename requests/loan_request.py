from request_ABC import RequestABC
from libraryBooks.library_book import LibraryBook
from libraryUsers.library_user import LibraryUser

class LoanRequest(RequestABC):
    
    def __init__(self, book: LibraryBook, user: LibraryUser, accepted: bool):
        self._book = book
        self._user = user
        self._accepted = accepted
        
    @property
    def book(self):
        return self._book
    
    @property
    def accepted(self):
        return self._accepted
    
    @property
    def user(self):
        return self._user
        
 