import abc

class AbsFactory(abc):

    @abc.abstractclassmethod
    def create(self):
        pass