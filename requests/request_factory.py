from requests.library_reservation_request import ReservationRequest
from requests.library_return_request import ReturnRequest
from requests.loan_request import LoanRequest

from libraryUsers.library_user import LibraryUser
from libraryBooks.library_book import Book

class RequestFactory():

    def create_reservation_request(book : Book, user : LibraryUser, is_accepted : bool) -> ReservationRequest:
        return ReservationRequest(book, user, is_accepted)

    def create_return_request(book : Book, user : LibraryUser, is_accepted : bool) -> ReturnRequest:
        return ReturnRequest(book, user, is_accepted)

    def create_loan_request(book : Book, user : LibraryUser, is_accepted : bool) -> LoanRequest:
        return LoanRequest(book, user, is_accepted)