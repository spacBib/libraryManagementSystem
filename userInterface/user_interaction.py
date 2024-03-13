from libraryUsers.library_user import LibraryUser
from .user_action_factory import UserActionFactory
from .userActions import AbsUserAction
from .user_choice_selector import UserChoiceSelector

class UserInteraction():
    def __init__(self, user : LibraryUser) -> None:
        self._user = user

    def _get_action_list(self) -> list[AbsUserAction]:
        _factory = UserActionFactory()
        _action_list = _factory.create_list_of_all()
        _usable_action_list = []
        for _action in _action_list:

            # Requires some argument
            if not _action.is_usable():
                continue
            _usable_action_list.append(_action)

        return _usable_action_list
    
    def _request_user_action(self) -> bool:
        _action_list : list[AbsUserAction] = self._get_action_list()

        _action_name_list = []
        for _action in _action_list:
            _action_name_list.append(_action.name)

        _choice_selector = UserChoiceSelector()
        _choice_index = _choice_selector.get_user_choice(_action_name_list)

        _selected_action : AbsUserAction= _action_list[_choice_index]
        _selected_action.select_action()

        return _selected_action.ends_user_interaction()

    def start_user_interaction(self):
        while(True):
            _end_loop = self._request_user_action()
            if (_end_loop):
                break


