from libraryDatabase.database_connector import ConnectToDatabase
from libraryDatabase.info_getter import InfoGetter
from libraryBooks.library_book_factory import BookFactory
import requestAndResult.request_handler
import requestAndResult.search.search_factory
def main():
    
    
    fact = requestAndResult.search.search_factory.SearchFactory()
    req = fact.create_request("enable", 5)
    
    req_handler = requestAndResult.request_handler.RequestHandler()
    
    result = req_handler.handle_request(req)
    
    for book in result.results:
        book.print()
    
    
    
    
    
    # db_connect = ConnectToDatabase()
    # db_connect.connect_to_server()
    # db = db_connect.connect_to_database("library_management_system")
    # factory = BookFactory()
    
    # info_getter = InfoGetter(db)
    # info_list = info_getter.search_title("enable")
    # for dict in info_list:
    #     print(dict)
    #     book = factory.create_from_dict(dict)
    #     print(book.id)
    #     print(book.author)
    #     print(book.title)
    #     print(book.year)
    #     print(book.isbn)
    #     print(book.available)
    
main()