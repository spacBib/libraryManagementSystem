from faker import Faker
from datetime import datetime

class FakerItemCreator():
    def __init__(self) -> None:
            self._faker = Faker()
            
    def set_seed(self, seed : int):
        Faker.seed(seed)

    def get_fake_ISBN13(self) -> str:
          return self._faker.isbn13()
    
    def get_fake_name(self) -> str:
        return self._faker.name()
          
    def get_fake_address(self) -> str:
        return self._faker.address()
    
    def get_fake_book_title(self) -> str:
         return self._faker.bs()
    
    def get_fake_publishing_year(self, min : int, max : int) -> int:
        return self._faker.pyint(min_value = min, max_value = max)
    
    def get_fake_birthday(self) -> int:
        _date_time = self._faker.date_between()
        _date_string = _date_time.strftime("%Y/%m/%d")
        return _date_string