from designPatterns.factoryPattern.abs_factory import AbsFactory
from libraryUsers.library_user import LibraryUser

class UserFactory(AbsFactory):

    def create(self, id : int, name : str, address : str, email : str) -> LibraryUser:
        return LibraryUser(id, name, address, email)
