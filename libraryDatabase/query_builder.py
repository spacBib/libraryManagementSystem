from libraryUsers.library_user import LibraryUser
from libraryBooks.library_book import LibraryBook
class QueryBuilder(object):
    

    
    
    # Get all books that contains title
    @staticmethod
    def query_title(title: str) -> str:
        query = "SELECT ID, TITLE, AUTHOR, PUBLISHINGYEAR, ISBN, AVAILABILITY FROM BOOKS WHERE BOOKS.TITLE LIKE " + f"\"%{title}%\""
        return query
    
    @staticmethod
    def query_author(author: str) -> str:
        query = "SELECT ID, TITLE, AUTHOR, PUBLISHINGYEAR, ISBN, AVAILABILITY FROM BOOKS WHERE BOOKS.AUTHOR LIKE " + f"\"%{author}%\""
        return query

    # Get specific book
    @staticmethod
    def query_book_reservation(book: LibraryBook, user: LibraryUser) -> str:
        query = (
            f"SELECT BOOKS.ID, BOOKS.TITLE, BOOKS.AUTHOR, BOOKS.ISBN, BOOKS.AVAILABILITY "
            f"FROM BOOKS "
            f"JOIN RESERVATIONS ON BOOKS.ID = RESERVATIONS.BOOK_ID "
            f"JOIN USERS ON RESERVATIONS.USER_ID = USERS.ID "
            f"WHERE BOOKS.ID = {book.id} AND USERS.ID = {user.id}"
        )
        print("Generated Query:", query)
        return query

        # Get user
    @staticmethod
    def query_user(user_name: str) -> str:
        query = "SELECT ID, NAME, ADDRESS, EMAIL FROM USERS WHERE USUERS.NAME IS " + f"{user_name}"
        return query
    
    # BOOKCOPIES: table of individual books with status
    # BOOKTITLES: table of titles with author, year etc. info
    
    # @staticmethod
    # def query_title(title: str) -> str:
    #     base = "SELECT {} FROM {} JOIN {} {}"
    #     columns = "TITLE, AUTHOR, YEAR, STATUS"
    #     table1 = "BOOKCOPIES"
    #     table2 = "BOOKTITLES"
    #     on = "ON BOOKTITLES.TITLE LIKE %" + title + "%"
    #     query = base.format(columns, table1, table2, on)
    #     return query
    
    # # Get all books by an author
    # @staticmethod
    # def query_author(author: str) -> str:
    #     base = "SELECT {} FROM {} JOIN {} {}"
    #     columns = "TITLE, AUTHOR, YEAR, STATUS"
    #     table1 = "BOOKCOPIES"
    #     table2 = "BOOKTITLES"
    #     on = "ON BOOKTITLES.AUTHOR=" + author
    #     query = base.format(columns, table1, table2, on)
    #     return query
    
    # # Get info related to a user
    # @staticmethod
    # def query_user(user_id: int) -> str:
    #     base = "SELECT {} FROM {} WHERE ID={}"
    #     columns = "NAME, ADDRESS"
    #     table1 = "USERS"
    #     query = base.format(columns, table1, user_id)
    #     return query
    
    
    # # Update status of an individual copy of a book
    # @staticmethod
    # def update_status(book_id: int, new_status: str):
    #     # table of individual books: BOOKCOPIES
    #     # field of book status: STATUS
    #     # ID of book = ID
    #     base = "UPDATE BOOKCOPIES SET STATUS={} WHERE ID={}"
    #     query = base.format(new_status, book_id)
    #     return query
        

    
    

# def main():
#     print("\n")
#     print( QueryBuilder.query_title("Dune") )
#     print( QueryBuilder.query_author("Frank Herbert") )
#     print( QueryBuilder.query_user(14) )
#     print( QueryBuilder.update_status(23, "reserved") )
#     print("\n")
    
# main()