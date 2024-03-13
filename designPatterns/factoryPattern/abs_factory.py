import abc

class AbsFactory(abc.ABC):

    @abc.abstractclassmethod
    def create(self):
        pass