from .fakerAbsGenerator import FakerAbsGenerator

class FakerUserGenerator(FakerAbsGenerator):
    
    def get_data_headers(self) -> list[str]:
        return [
            "Name",
            "Birthday",
            "Addresse",
            "E-mail",
        ]

    def generate_item_data(self):
        _fake_name = self._item_creator.get_fake_name()
        _fake_birthday = self._item_creator.get_fake_birthday()
        _birthyear = int(_fake_birthday[0:4])

        return [
            _fake_name,
            _fake_birthday,
            self._item_creator.get_fake_address(),
            self._item_creator.get_fake_email(_fake_name, _birthyear)
        ]