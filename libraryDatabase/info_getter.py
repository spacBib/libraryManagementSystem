from datetime import datetime
from mysql.connector import MySQLConnection
from libraryDatabase.query_builder import QueryBuilder

class InfoGetter(object):
    
    
    def __init__(self, mysql_connection: MySQLConnection):
        self._mysql_connection = mysql_connection
    
    # Takes a title and returns information from the database
    def search_title(self, title: str) -> dict:
        query = QueryBuilder().query_title(title)
        cursor = self._mysql_connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    def search_book_id(self, book_id: int) -> dict:
        query = QueryBuilder().query_book_id(book_id)
        cursor = self._mysql_connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchone()
    
    # # Takes an author and returns information from the database
    # def search_author(self, author: str) -> dict:
    #     query = QueryBuilder().query_title(author)
    #     cursor = self._mysql_connection.cursor(dictionary=True)
    #     cursor.execute(query)
    #     return cursor.fetchall()

    # Reserve a book
    def reserve_book(self, book_id: int, user_id: int) -> bool:
        try:
            today = str(datetime.now().strftime('%Y-%m-%d'))
            query = QueryBuilder.query_book_reservation(book_id, user_id, today)

            cursor = self._mysql_connection.cursor()
            cursor.execute(query)

            self._mysql_connection.commit()
            cursor.close()
            
            print("Book reserved successfully.")
            return True
        except Exception as e:
            print(f"Error reserving book: {e}")

    # Loan a book
    def loan_book(self, book_id: int, user_id: int) -> None:
        try:
            today = str(datetime.now().strftime('%Y-%m-%d'))
            query = QueryBuilder.query_book_reservation(book_id, user_id, today)

            cursor = self._mysql_connection.cursor()
            cursor.execute(query)

            self._mysql_connection.commit()
            cursor.close()

            print("Book loaned successfully.")
        except Exception as e:
            print(f"Error loaning book: {e}")


    