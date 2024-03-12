from mysql.connector import MySQLConnection
from libraryDatabase.query_builder import QueryBuilder

class InfoGetter(object):
    
    
    def __init__(self, mysql_connection: MySQLConnection):
        self._mysql_connection = mysql_connection
    
    # Takes a title and returns information from the database
    def search_title(self, title: str) -> dict:
        query = QueryBuilder().query_title(title)
        print(query)
        cursor = self._mysql_connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    # Takes an author and returns information from the database
    def search_author(self, author: str) -> dict:
        query = QueryBuilder().query_title(author)
        cursor = self._mysql_connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    
    