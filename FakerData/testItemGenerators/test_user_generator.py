from .abs_test_item_generator import absTestItemGenerator

from libraryUsers.library_user_factory import LibraryUserFactory
from ..faker_user_generator import FakerUserGenerator

class absTestItemGenerator(absTestItemGenerator):

    def create():
        factory = FakerUserGenerator()
        userData = factory.generate_item_data()
        