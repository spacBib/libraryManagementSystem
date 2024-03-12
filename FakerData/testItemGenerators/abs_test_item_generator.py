import abc

class absTestItemGenerator(abc.ABC):

    @abc.abstractstaticmethod
    def create():
        pass