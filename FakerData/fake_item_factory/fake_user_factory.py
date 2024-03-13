from designPatterns.factoryPattern.abs_factory import AbsFactory
from libraryUsers.library_user_factory import UserFactory
from libraryUsers.library_user import LibraryUser

from fakerData.faker_user_generator import FakerUserGenerator

import random

class FakeUserFactory(AbsFactory):

    def create(self, _fakeID):
        return self._create(_fakeID)

    def _create(self, fakeId : int) -> LibraryUser:
        faker = FakerUserGenerator()
        factory = UserFactory()

        strList = faker.generate_item_data()
        strListClean = []
        for string in strList:
            strListClean.append(string.replace("\"",""))
        
        user = factory.create(
            fakeId,
            strList[0],
            strList[1],
            strList[2]
        )
        
        return user
