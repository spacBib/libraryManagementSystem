# Library Management System

The goal of this project is get familiar with design patterns, OOP, and SOLID principles 
by developing a management system for a library. 
The library system should be capable of looking up books, loan books, return books, and reserve books.

## Description

The desired functionality have been achieved, where the core parts are the database, library interaction, and user interface

The database contains information about the contents of library such as 
users registered, books available, books lent, books reserved, and books returned.
The database is queried by functions in order to create, read, update or delete the contents of the library

Library interaction is made possible by querying the database. The information from the query is used by various functions in order 
to fulfill a user request such as search, loan, reserve, or return.

The User interface prompts a user with certain options the user can take and depending on what they choose different possibility opens op.
The request is completed by combining the functionality from the database and library interaction to return a result to the user.

## Getting Started

### Dependencies

* Windows 10
* Visual Studio Code 1.86
* MySQL server 8.3.0
* MySQL Workbench 8.0.36
* Python 3.9
* The necessary libraries can be found in the requirements.txt file

### Installing & Executing program

* Download the zip/clone from https://github.com/spacBib/libraryManagementSystem
* Unzip at a desired location
* In visual studio code go to "File -> Open folder" and choose the libraryManagementSystem folder
* In the VS code libraryManagementSystem project terminal navigate (cd) to the "requirements.txt" file and run:
```
pip install -r requirements.txt
```
* Afterward navigate back to your project root and go the script:
"libraryDatabase -> database_connector.py" and edit it to fit your local MySQL server
* Next go "libraryDatabase -> main_database_builder.py" and run the script there to set up the library database
* Now go to "main.py" script in the project and run it.

## Authors & Help

[@Mfly87](https://github.com/Mfly87)
[@Niels87](https://github.com/Niels87)
[@Resh404](https://github.com/Resh404)