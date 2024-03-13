from .abs_user_action import AbsUserAction

from libraryUsers.library_user import LibraryUser

from libraryDatabase.database_connector import ConnectToDatabase
from libraryDatabase.info_getter import InfoGetter
from libraryBooks.library_book_factory import BookFactory
import requestAndResult.request_handler
import requestAndResult.search.search_factory


class UserActionSearch(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Search"
    
    @property
    def priority(self) -> int:
        return 1
    
    def is_usable(self, userInteraction) -> bool:
        return True

    def select_action(self, userInteraction) -> None:
        _input = input("Enter search string: ")
        _user : LibraryUser = userInteraction.user

        
        fact = requestAndResult.search.search_factory.SearchFactory()
        req = fact.create_request(_input, _user.id)
        
        req_handler = requestAndResult.request_handler.RequestHandler()
        
        result = req_handler.handle_request(req)
        
        print("")
        print("The following books matched your search:")
        _books_found = []
        for _book in result.results:
            print("\"" + _book.title + "\" by " + _book.author + " with following ISBN: " + _book.isbn )
            _books_found.append(_book)

        userInteraction.set_prev_search_results(_books_found)


        
    def ends_user_interaction(self) -> bool:
        pass