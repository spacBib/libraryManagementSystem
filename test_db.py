from libraryDatabase.database_connector import ConnectToDatabase
from libraryDatabase.info_getter import InfoGetter
from libraryBooks.library_book_factory import BookFactory

def main():
    db = ConnectToDatabase("localhost", "root", "Kom12345", 3306)
    db_con = db.connect_to_database("library_management_system")
    factory = BookFactory()
    
    info_getter = InfoGetter(db_con)
    info_list = info_getter.search_title("enable")
    for dict in info_list:
        print(dict)
        book = factory.create_from_dict(dict)
        print(book.id)
        print(book.author)
        print(book.title)
        print(book.year)
        print(book.isbn)
        print(book.available)
    
main()