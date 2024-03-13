from .abs_user_action import AbsUserAction

from libraryBooks.library_book import LibraryBook

from userInterface.user_choice_selector import UserChoiceSelector

class UserActionLoan(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Loan"
    
    @property
    def priority(self) -> int:
        return 0
    
    def is_usable(self, userInteraction) -> bool:
        return userInteraction.previous_search_result

    def select_action(self, userInteraction) -> None:
        print("Which book do you want to loan?")       

        _book_list : list[LibraryBook] = userInteraction.previous_search_result
        _name_list = []
        for _book in _book_list:
            _name_list.append(_book.to_string())

        _choice_selector = UserChoiceSelector()
        _choice_index = _choice_selector.get_user_choice(_name_list)
        
        userInteraction.set_prev_search_results([])
        
    def ends_user_interaction(self) -> bool:
        pass