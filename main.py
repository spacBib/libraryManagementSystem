import csv
from libraryDatabase.database_connector import ConnectToDatabase
from libraryDatabase.create_database_tables import CreateLibraryTables

if __name__ == "__main__":
    mysql_server = ConnectToDatabase("localhost", "root", "Kom12345", 3306)
    database_connection = mysql_server.connect_to_database("library_management_system")
    sql_database_table_creator = CreateLibraryTables()

    column_names_books = ["id", "title", "author", "publishingYear", "ISBN", "availability"]
    column_types_books = ["INT AUTO_INCREMENT PRIMARY KEY", "VARCHAR(255)", "VARCHAR(255)", "INT",
                          "VARCHAR(255)", "VARCHAR(255)"]
    library_book_data = []
    library_user_data = []

    with open("fakeBooks.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        for row in reader:
            row.append("TRUE")
            library_book_data.append(tuple(row))

    sql_database_table_creator.create_table("books", column_names_books, column_types_books,
                                            library_book_data, database_connection)

    column_names_users = ["id", "name", "address", "email"]
    column_types_users = ["INT AUTO_INCREMENT PRIMARY KEY", "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)"]

    with open("fakeUsers.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        for row in reader:
            library_user_data.append(tuple(row))

    sql_database_table_creator.create_table("users", column_names_users, column_types_users,
                                            library_user_data, database_connection)
