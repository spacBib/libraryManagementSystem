from .abs_user_action import AbsUserAction

class UserActionSearch(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Search"
    
    @property
    def priority(self) -> int:
        return 0
    
    def is_usable(self) -> None:
        return True

    def select_action(self) -> None:
        pass