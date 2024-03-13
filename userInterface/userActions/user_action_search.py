from .abs_user_action import AbsUserAction

class UserActionSearch(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Search"
    
    @property
    def priority(self) -> int:
        return 0
    
    def is_usable(self) -> bool:
        return True

    def select_action(self) -> None:
        print("Seaching...")
        print("Seaching...")
        print("Seaching...")
        
    def ends_user_interaction(self) -> bool:
        pass