from libraryUsers.library_user import LibraryUser
from .user_action_factory import UserActionFactory
from .userActions import AbsUserAction

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
    
    def request_user_action(self) -> None:
        pass



