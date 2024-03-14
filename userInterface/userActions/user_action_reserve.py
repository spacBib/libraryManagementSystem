from .abs_user_action import AbsUserAction

from libraryBooks.library_book import LibraryBook
from libraryUsers.library_user import LibraryUser

from userInterface.user_choice_selector import UserChoiceSelector

from requestAndResult.reservation.reservation_factory import ReservationFactory
from requestAndResult.reservation.reservation_result import ReservationResult
from requestAndResult.request_handler import RequestHandler


class UserActionReserve(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Reserve"
    
    @property
    def priority(self) -> int:
        return 10
    
    def is_usable(self, userInteraction) -> bool:
        return userInteraction.previous_search_result

    def select_action(self, userInteraction) -> None:
        print("Which book do you want to reserve?")       

        _user : LibraryUser = userInteraction.user

        _book_list : list[LibraryBook] = userInteraction.previous_search_result
        _name_list = ["None"]
        for _book in _book_list:
            _name_list.append(_book.to_string())

        _choice_selector = UserChoiceSelector()
        _choice_index = _choice_selector.get_user_choice(_name_list) - 1
        
        if _choice_index < 0:
            return

        _selected_book : LibraryBook = _book_list[_choice_index]

        fact = ReservationFactory()
        req = fact.create_request(_selected_book.id, _user.id)
        
        req_handler = RequestHandler()
        
        result : ReservationResult = req_handler.handle_request(req)

        userInteraction.user.add_book(_selected_book)
        userInteraction.set_prev_search_results([])

        
    def ends_user_interaction(self) -> bool:
        pass