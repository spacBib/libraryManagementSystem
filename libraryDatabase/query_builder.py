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

    # Reserve book
    @staticmethod
    def query_book_reservation(book_id: int, user_id: int, date: str) -> str:
        query = (
            f"INSERT INTO RESERVATIONS (BOOK_ID, USER_ID, RESERVATION_DATE) "
            f"VALUES ({book_id}, {user_id}, \"{date}\")"
        )
        return query

    # loan book
    @staticmethod
    def query_book_loan(book_id: int, user_id: int, date: str) -> str:
        query = (
            f"INSERT INTO BOOK_LOANS (BOOK_ID, USER_ID, LOAN_DATE) "
            f"VALUES ({book_id}, {user_id}, \"{date}\")"
        )
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