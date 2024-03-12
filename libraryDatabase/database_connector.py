from libraryUtils.singleton_for_database import Singleton
import mysql.connector


class ConnectToDatabase(Singleton):
    # define database variables
    def __init__(self, host_name: str, user_name: str, password: str, port: int):
        self.host_name = host_name
        self.user_name = user_name
        self.password = password
        self.port = port

    def connect_to_server(self) -> mysql.connector:
        try:
            # Connect to the server
            my_database = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                password=self.password,
                port=self.port
            )
            return my_database
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    def connect_to_database(self, database_name: str) -> mysql.connector.connection.MySQLConnection:
        try:
            # Connect to the specified server
            my_database = self.connect_to_server()

            # Check if the database exists
            cursor = my_database.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

            # Switch to the specified database
            cursor.execute(f"USE {database_name}")
            cursor.close()  # Close the cursor after switching the database

            return my_database
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise
