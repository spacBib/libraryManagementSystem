import abc

class AbsUserAction(abc.ABC):
    
    @abc.abstractclassmethod
    def perform_action(self):
        pass