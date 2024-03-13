import requestAndResult.search.search_factory 
import requestAndResult.loan.loan_factory 
import requestAndResult.returns.returns_factory 
import requestAndResult.reservation.reservation_factory
from requestAndResult import factory_abc
import requestAndResult
class FactoryFinder():
    
    @staticmethod
    def get_concrete_factory(factory_type: str) -> factory_abc.ResultRequestFactoryABC:
        match factory_type :
            case "search":
                return requestAndResult.search.search_factory.SearchFactory()
            case "loan":
                return requestAndResult.loan.loan_factory.LoanFactory()
            case "reservation":
                return requestAndResult.reservation.reservation_factory.ReservationFactory()
            case "returns":
                return requestAndResult.returns.returns_factory.ReturnsFactory()
            case _:
                print("no such result/request type") # throw exception?!