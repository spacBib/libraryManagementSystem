from designPatterns.factoryPattern.abs_factory import AbsFactory
from libraryBooks.library_book import Book

class BookFactory(AbsFactory):

    def create(id : int, author : str, title : str, year : int, isbn : str, copies : int) -> Book:
        return Book(id, author, title, year, isbn, copies)
