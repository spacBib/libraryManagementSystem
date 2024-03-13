from .abs_user_action import AbsUserAction

class UserActionCancel(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Cancel"

    @property
    def priority(self) -> int:
        return -1000    

    def is_usable(self, userInteraction) -> bool:
        return True

    def select_action(self, userInteraction) -> None:
        print("Have a nice day!")
        
    def ends_user_interaction(self) -> bool:
        return True