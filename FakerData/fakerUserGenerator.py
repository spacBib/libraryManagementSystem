from fakerAbsGenerator import FakerAbsGenerator

class FakerUserGenerator(FakerAbsGenerator):
    
    def get_data_headers(self) -> list[str]:
        return [
            "Name",
            "Birthday",
            "Addresse",
        ]

    def generate_item_data(self):
        return [
            self._item_creator.get_fake_name(),
            self._item_creator.get_fake_birthday(),
            self._item_creator.get_fake_address()
        ]
    

a = FakerUserGenerator()
print(a.get_data_headers())
for i in range(20):
    print(a.generate_item_data())