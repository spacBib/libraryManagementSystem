import abc

class RequestABC(abc.ABC):
    
    # the requested book (instance of Book-class)
    @property
    @abc.abstractmethod
    def book(self):
        pass
    
    # was the request accepted (bool)
    @property
    @abc.abstractmethod
    def accepted(self):
        pass
    
    # the user who made the request (instance of LibraryUser-class)
    @property
    @abc.abstractmethod
    def user(self):
        pass
        
    
    
    