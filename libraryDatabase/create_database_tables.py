from typing import List, Tuple
import mysql.connector


class CreateLibraryTables:
    def create_table(self, table_name: str, column_names: List[str], column_types: List[str],
                     library_data: List[Tuple], database_connector: mysql.connector.MySQLConnection) -> None:
        try:
            # Connect to the database
            with database_connector.cursor() as cursor:
                # Link data names with data types
                column_definitions = [f"{col_name} {col_type}" for col_name, col_type in
                                      zip(column_names, column_types)]
                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_definitions)})"
                cursor.execute(create_table_query)

                # Remove ID entry and insert data into the table
                column_names = column_names[1:]
                insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"
                cursor.executemany(insert_query, library_data)

            # Commit changes
            database_connector.commit()

            print(f"Table '{table_name}' created successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")
            raise








