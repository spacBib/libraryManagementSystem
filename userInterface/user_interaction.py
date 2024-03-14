from libraryUsers.library_user import LibraryUser
from libraryBooks.library_book import LibraryBook
from .user_action_factory import UserActionFactory
from .userActions import AbsUserAction
from .user_choice_selector import UserChoiceSelector

class UserInteraction():
    def __init__(self, user : LibraryUser) -> None:
        self._user = user
        self._prev_search_results = []

    @property
    def user(self):
        return self._user

    @property
    def previous_search_result(self):
        return self._prev_search_results

    def set_prev_search_results(self, book_list : list[LibraryBook]):
        if not isinstance(book_list, list):
            return
        self._prev_search_results.clear()
        for _book in book_list:
            if isinstance(_book, LibraryBook):
                self._prev_search_results.append(_book)

    def _get_action_list(self) -> list:
        _factory = UserActionFactory()
        _action_list = _factory.create_list_of_all()
        _usable_action_list = []
        for _action in _action_list:
            if not _action.is_usable(self):
                continue
            _usable_action_list.append(_action)

        return _usable_action_list
    
    def _request_user_action(self) -> bool:
        _action_list = self._get_action_list()

        _action_name_list = []
        for _action in _action_list:
            _action_name_list.append(_action.name)

        _choice_selector = UserChoiceSelector()
        _choice_index = _choice_selector.get_user_choice_from_name_list(_action_name_list)

        _selected_action = _action_list[_choice_index]
        _selected_action.select_action(self)

        return _selected_action.ends_user_interaction()

    def start_user_interaction(self):
        print("")
        print("Hello " + self.user.name)
        while(True):
            print("Welcome to SPAC Library")
            _end_loop = self._request_user_action()
            if (_end_loop):
                break
            print("")
            print("")


