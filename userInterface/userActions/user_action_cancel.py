from .abs_user_action import AbsUserAction

class UserActionCancel(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Cancel"

    @property
    def priority(self) -> int:
        return -1000    

    def is_usable(self) -> bool:
        return True

    def select_action(self) -> None:
        print("Have a nice day!")
        
    def ends_user_interaction(self) -> bool:
        return True