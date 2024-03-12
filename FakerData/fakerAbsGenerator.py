from fakerData.fakerItemCreator import FakerItemCreator
import abc

class FakerAbsGenerator(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self._item_creator = FakerItemCreator()

    @property
    def item_creator(self):
        return self._item_creator

    def set_seed(self, seed: int):
        self._item_creator.set_seed(seed)

    @abc.abstractmethod
    def get_data_headers(self) -> list[str]:
        pass

    @abc.abstractmethod
    def generate_item_data(self) -> list:
        pass