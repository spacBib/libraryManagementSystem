from designPatterns.factoryPattern.abs_factory import AbsFactory
from libraryBooks.library_book_factory import BookFactory
from libraryBooks.library_book import LibraryBook

from fakerData.faker_book_generator import FakerBookGenerator

import random

class FakeBookFactory(AbsFactory):

    def create(self, fakeId : int, is_available : bool) -> LibraryBook:
        faker = FakerBookGenerator()
        factory = BookFactory()

        strList = faker.generate_item_data()
        strListClean = []
        for string in strList:
            strListClean.append(string.replace("\"",""))
        
        book = factory.create(
            fakeId, 
            strListClean[1],
            strListClean[0],
            strListClean[2],
            strListClean[3],
            is_available
            )
        
        return book
