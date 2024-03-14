# Library Management System

Det goal of this project is get familiar with design patterns, OOP, and SOLID principles 
by developing a management system for a library. 
The library system should be capable of look up books, loan books, return books, and reserve books.

## Description

The desired functionality have been archived, where the core parts are the database, library interaction, and user interface

The database contains information about the contents of library such as 
users registered, books available, books lent, books reserved, and books returned.
The database is queried by functions in order to create, read, update or delete the contents of the library

Library interaction is made possible by querying the database. The information from the query is used by various functions in order 
to fulfill a user request such as search, loan, reserve, or return.

The User interface prompts a user with certain options the user can take and depending on what they choose different possibility opens op.
The request is completed by combing the functionality from the database and library interaction and result is returned to the user.

## Getting Started

### Dependencies

* Visual Studio Code 1.87.2
* The necessary libraries can be found in the requirements.txt file
* Windows 10

### Installing & Executing program

* Download the zip/clone from https://github.com/spacBib/libraryManagementSystem
* Unzip at a desired location
* In visual studio code go to File -> Open folder and choose the libraryManagementSystem folder
* In the VS code libraryManagementSystem project terminal navigate (cd) to the requirements.txt file and run:
```
pip install -r requirements.txt
```
* Afterward navigate back to your project root and go the script:
libraryDatabase -> database_connector.py and edit it to fit your local MySQL server
* Next go libraryDatabase -> main_database_builder.py and run the script there to set up the library database
* Now go to ???? and run the user interface script

## Authors & Help

[@Mfly87](https://github.com/Mfly87)
[@Niels87](https://github.com/Niels87)
[@Resh404](https://github.com/Resh404)
