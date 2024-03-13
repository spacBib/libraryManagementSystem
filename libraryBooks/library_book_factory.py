from designPatterns.factoryPattern.abs_factory import AbsFactory
from libraryBooks.library_book import LibraryBook

class BookFactory(AbsFactory):

    def create_from_dict(self, info: dict):
        try:
            id = info.get("ID")
        except:
            id = None
        
        try:
            title = info.get("TITLE")
        except:
            title = None
        
        try:
            author = info.get("AUTHOR")
        except:
            author = None
        
        try:
            year = info.get("PUBLISHING_YEAR")
        except:
            year = None
        
        try:
            isbn = info.get("ISBN")
        except:
            isbn = None
        try: 
            available = info.get("AVAILABILITY")
        except:
            available = None
        
        book = self.create(id, author, title, year, isbn, available)
        return book
    
    def create(self, id: int, author : str, title : str, year : int, isbn : str, available: bool) -> LibraryBook:
        return LibraryBook(id, author, title, year, isbn, available)
