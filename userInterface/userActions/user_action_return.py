from .abs_user_action import AbsUserAction

from userInterface.user_choice_selector import UserChoiceSelector

class UserActionReturn(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Return"
    
    @property
    def priority(self) -> int:
        return 2
    
    def is_usable(self, userInteraction) -> bool:
        return userInteraction.user.books

    def select_action(self, userInteraction) -> None:
        print("Which book do you want to return?")       

        _user = userInteraction.user

        _book_list = _user.books
        _name_list = ["None"]
        for _book in _book_list:
            _name_list.append(_book.to_string())

        _choice_selector = UserChoiceSelector()
        _choice_index = _choice_selector.get_user_choice_from_name_list(_name_list) - 1
        
        if _choice_index < 0:
            return

        _selected_book = _book_list[_choice_index]
        _user.remove_book(_selected_book)

        
    def ends_user_interaction(self) -> bool:
        pass