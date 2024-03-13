from abc import ABC, abstractmethod

class ResultRequestFactoryABC(ABC):
    
    @abstractmethod
    def create_request():
        pass
    
    
    @abstractmethod
    def create_result():
        pass