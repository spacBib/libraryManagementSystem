

class Book(object):
    
    def __init__(self, 
                 author: str,
                 title: str,
                 year: int,
                 isbn: str,
                 copies: int 
                 ):
        self._author = author
        self._title = title
        self._year = year
        self._isbn = isbn
        self._copies = copies 

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    # nr of copies of this title in the library
    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value):
        self._copies = value
    
    # unique id for each copy of a book
    _id: str
    _author: str
    _title: str
    _year: int
    # id for the title, not the individual copy of a book
    _isbn: str
    # copies of this book title in the library
    _copies: int    
    
    
    def print(self):
        print("Author: " + self.author)
        print("Title: " + self.author)
        print("Year: " + str(self.year))
        print("ISBN: " + self.isbn)
