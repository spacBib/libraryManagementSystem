import abc

class AbsFactory(abc.ABC):

    @abc.abstractclassmethod
    def _create(self):
        pass