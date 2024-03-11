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
    
    def get_fake_email(self, fullName : str, birthyear : int):
        _domain = self._faker.free_email_domain()
        _id = self._get_fake_email_id(fullName, birthyear)
        return _id + "@" + _domain


    def _nameStyle_a(self, fullName : str, filler : str):
        _splitName = fullName.split(" ")
        return filler.join(_splitName)
        
    def _nameStyle_b(self, fullName : str, filler : str):
        _splitName = fullName.split(" ")            
        return filler.join([_splitName[0][0],_splitName[1]])
    
    def _nameStyle_c(self, fullName : str, filler : str):
        _splitName = fullName.split(" ")

        _first_name = _splitName[0]
        del _splitName[0]
        _rest_name = "".join(_splitName)

        return filler.join([_first_name[0],_rest_name[0:3]])
    
    def _get_fake_email_id(self, fullName : str, birthyear : int) -> str:
        _fillers = [".","-","_",""]
        _fillerIndex = self._faker.pyint(min_value = 0, max_value = len(_fillers)-1)
        _filler = _fillers[_fillerIndex]
         
        _styleFuncs = [
             self._nameStyle_a, 
             self._nameStyle_b,
             self._nameStyle_c, 
             ]
        _styleFuncIndex = self._faker.pyint(min_value = 0, max_value = len(_styleFuncs)-1)
        _styleFunc = _styleFuncs[_styleFuncIndex]

        _id_name = _styleFunc(fullName, _filler)

        _yearStyles = [
            "",
            str(birthyear),
            str(birthyear%100).zfill(2)
        ]
        _yearStyleIndex = self._faker.pyint(min_value = 0, max_value = len(_yearStyles)-1)
        
        _id_year = _yearStyles[_yearStyleIndex]
        return _id_name + _id_year