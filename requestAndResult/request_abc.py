from abc import ABC, abstractmethod

class RequestABC(ABC):
    
    @abstractmethod
    def __init__(self, request_type: str):
        self._request_type = request_type
    
    @property
    def request_type(self):
        return self._request_type
    
    