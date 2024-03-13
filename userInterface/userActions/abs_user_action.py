import abc

class AbsUserAction(abc.ABC):

    @abc.abstractproperty
    def name(self) -> str:
        pass

    @abc.abstractproperty
    def priority(self) -> int:
        pass

    @abc.abstractclassmethod
    def is_usable(self) -> None:
        pass

    @abc.abstractclassmethod
    def select_action(self) -> None:
        pass