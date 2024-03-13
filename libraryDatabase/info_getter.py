from typing import List

from mysql.connector import MySQLConnection
from libraryDatabase.query_builder import QueryBuilder
from libraryUsers.library_user import LibraryUser
from libraryBooks.library_book import LibraryBook

class InfoGetter(object):
    
    
    def __init__(self, mysql_connection: MySQLConnection):
        self._mysql_connection = mysql_connection
    
    # Takes a title and returns information from the database
    def search_title(self, title: str) -> dict:
        query = QueryBuilder().query_title(title)
        cursor = self._mysql_connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    # Takes an author and returns information from the database
    def search_author(self, author: str) -> dict:
        query = QueryBuilder().query_title(author)
        cursor = self._mysql_connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()

    # Reserver a book
    def reserve_book(self, book: LibraryBook, user: LibraryUser) -> List[tuple]:
        try:
            book_query = QueryBuilder.query_book_reservation(book, user)
            cursor = self._mysql_connection.cursor(dictionary=True)

            print("Executing Query:", book_query)
            cursor.execute(book_query)

            result = cursor.fetchall()

            cursor.close()

            return result
        except Exception as e:
            print(f"Error reserving book: {e}")
            return None


    