import search.search_factory, loan.loan_factory, returns.returns_factory, reservation.reservation_factory
from requestAndResult import factory_abc

class FactoryFinder():
    
    @staticmethod
    def get_concrete_factory(self, factory_type: str) -> factory_abc.ResultRequestFactoryABC:
        match factory_type :
            case "search":
                return search.search_factory.SearchFactory()
            case "loan":
                return loan.loan_factory.LoanFactory()
            case "reservation":
                return reservation.reservation_factory.ReservationFactory()
            case "return":
                return returns.returns_factory.ReturnsFactory()
            case _:
                print("no such result/request type") # throw exception?!