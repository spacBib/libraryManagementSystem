import abc
from logger.abs_observer import AbsObserver

class AbsObserverSubject(abc.ABC):
    _observers : dict[AbsObserver] = {}

    @abc.abstractclassmethod
    def attach(self, observer : AbsObserver) -> None:
        if not isinstance(observer, AbsObserver):
            raise TypeError("Observer was not derived from AbsObserver")
        self._observers[observer] |= {observer}

    def detach(self, observer : AbsObserver) -> None:
        self._observers[observer] -= {observer}

    def notify(self, value = None) -> None:
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)
