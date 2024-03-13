from .abs_user_action import AbsUserAction

from fakerData.fake_item_factory import FakeBookFactory

class UserActionFakeSearch(AbsUserAction):
    
    @property
    def name(self) -> str:
        return "Search"
    
    @property
    def priority(self) -> int:
        return 1 + 1000
    
    def is_usable(self, userInteraction) -> bool:
        return True

    def select_action(self, userInteraction) -> None:
        print("Seaching...")
        print("Seaching...")
        print("Seaching...")
        print("")
        print("Our search function seems to not be implimented.")
        print("Perhaps these books will be of interest:")
        print("")
        _fake_book_factory = FakeBookFactory()
        _fake_books = []
        for i in range(5):
            _fake_book = _fake_book_factory.create(i, True)
            _fake_books.append(_fake_book)
            print("\"" + _fake_book.title + "\" by " + _fake_book.author + " with following ISBN: " + _fake_book.isbn )
        
        userInteraction.set_prev_search_results(_fake_books)


        
    def ends_user_interaction(self) -> bool:
        pass