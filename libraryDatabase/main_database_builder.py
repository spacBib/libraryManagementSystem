import csv
from libraryDatabase.database_connector import ConnectToDatabase
from libraryDatabase.create_database_tables import CreateLibraryTables
from libraryBooks.library_book import LibraryBook
from libraryUsers.library_user import LibraryUser
from libraryDatabase.info_getter import InfoGetter

if __name__ == "__main__":
    mysql_server = ConnectToDatabase()
    database_connection = mysql_server.connect_to_database("library_management_system")
    sql_database_table_creator = CreateLibraryTables()
    query_database = InfoGetter(database_connection)
    #a_user = LibraryUser(1, "April Lawson", "15241 Brown Views Suite 765", "April-Lawson2007@yahoo.com")
    #_book = LibraryBook(1, "utilize bleeding-edge web services", "Christopher Ashley", 2018, "978-0-678-87237-6", "TRUE")

    #query_database.reserve_book(a_user, a_book)

    # column_names_books = ["id", "title", "author", "publishing_year", "ISBN", "availability"]
    # column_types_books = ["INT AUTO_INCREMENT PRIMARY KEY", "VARCHAR(255)", "VARCHAR(255)", "INT",
    #                       "VARCHAR(255)", "VARCHAR(255)"]
    # library_book_data = []
    # library_user_data = []
    #
    # with open("fakeBooks.csv", 'r') as file:
    #     reader = csv.reader(file)
    #     next(reader)  # Skip the header line
    #     for row in reader:
    #         row.append("TRUE")
    #         library_book_data.append(tuple(row))
    #
    # sql_database_table_creator.create_table("books", column_names_books, column_types_books,
    #                                         library_book_data, database_connection)
    #
    # column_names_users = ["id", "name", "address", "email"]
    # column_types_users = ["INT AUTO_INCREMENT PRIMARY KEY", "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)"]
    #
    # with open("fakeUsers.csv", 'r') as file:
    #     reader = csv.reader(file)
    #     next(reader)  # Skip the header line
    #     for row in reader:
    #         library_user_data.append(tuple(row))
    #
    # sql_database_table_creator.create_table("users", column_names_users, column_types_users,
    #                                         library_user_data, database_connection)
    #
    # column_name_book_reservation = ["id", "book", "user", "date"]
    # column_type_book_reservation = ["INT AUTO_INCREMENT PRIMARY KEY", "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)"]
    #
    # sql_database_table_creator.create_table("reservations", column_name_book_reservation,
    #                                         column_type_book_reservation, [], database_connection)
    #
    # column_name_book_loan = ["id", "book", "user", "loan_date", "due_date", "status"]
    # column_type_book_loan = ["INT AUTO_INCREMENT PRIMARY KEY", "VARCHAR(255)", "VARCHAR(255)",
    #                          "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)"]
    #
    # sql_database_table_creator.create_table("book_loans", column_name_book_loan,
    #                                         column_type_book_loan, [], database_connection)

    sql_database_table_creator.create_table("reservations", [],
                                             [], [], database_connection)
