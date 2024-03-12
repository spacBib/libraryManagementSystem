from libraryDatabase.database_connector import ConnectToDatabase
from typing import List, Tuple
import mysql.connector


class CreateLibraryTables:
    def create_table(self, database_name: str, table_name: str, column_names: List[str], column_types: List[str],
                     library_data: List[Tuple], server_connector: ConnectToDatabase) -> None:
        try:
            # Connect to the server
            my_database = server_connector.connect_to_database(database_name)
            my_database.database = database_name

            # Create a cursor object
            cursor = my_database.cursor()

            # Create the database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

            # Switch to the specified database
            cursor.execute(f"USE {database_name}")

            # Create the product table
            column_definitions = []
            for col_name, col_type in zip(column_names, column_types):
                column_definitions.append(f"{col_name} {col_type}")
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_definitions)})"
            cursor.execute(create_table_query)

            # Commit changes and close cursor and connection
            my_database.commit()

            # Insert product data into the table
            insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"
            cursor.executemany(insert_query, library_data)

            my_database.commit()
            cursor.close()
            my_database.close()

            print(f"Storage database '{database_name}' created successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating storage database: {e}")