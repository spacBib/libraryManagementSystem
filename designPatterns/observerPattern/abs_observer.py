import abc

class AbsObserver(abc.ABC):

    @abc.abstractclassmethod
    def update(self, value) -> None:
        pass