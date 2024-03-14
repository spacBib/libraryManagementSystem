from fakerData.faker_abs_generator import FakerAbsGenerator

class FakerBookGenerator(FakerAbsGenerator):
    
    def get_data_headers(self) -> list[str]:
        return [
            "title",
            "author",
            "publishingYear",
            "ISBN" 
        ]

    def generate_item_data(self):
        return [
            self.item_creator.get_fake_book_title(),
            self._item_creator.get_fake_name(),
            str(self._item_creator.get_fake_publishing_year(1990,2024)),
            self._item_creator.get_fake_ISBN13()
        ]