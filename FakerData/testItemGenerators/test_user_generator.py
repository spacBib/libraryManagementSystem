from .abs_test_item_generator import absTestItemGenerator

from libraryUsers.library_user import LibraryUser
from libraryUsers.library_user_factory import LibraryUserFactory
from ..faker_user_generator import FakerUserGenerator

class absTestItemGenerator(absTestItemGenerator):

    def create() -> LibraryUser:
        faker = FakerUserGenerator()
        userData = faker.generate_item_data()

        cleanedData = []
        for data in userData:
            cleanedData.append(data.replace("\"",""))

        user = LibraryUserFactory.create(1, cleanedData[0], cleanedData[1], cleanedData[2])
        return user
        
