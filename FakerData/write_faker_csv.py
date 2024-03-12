from fakerData.faker_abs_generator import FakerAbsGenerator

from fakerData.faker_book_generator import FakerBookGenerator
from fakerData.faker_user_generator import FakerUserGenerator

class WriteFakerCSV():

    @staticmethod
    def write_csv_file(filename : str, generator : FakerAbsGenerator, lines : int, addHeader : bool = True, delimiter : str = ","):
        
        with open(filename, "w") as file:
            if addHeader:
                headerItems = generator.get_data_headers()
                text = delimiter.join(headerItems) + "\n"
                file.write(text)

            for i in range(lines):
                rowItems = generator.generate_item_data()
                text = delimiter.join(rowItems) + "\n"
                file.write(text)
    
    @staticmethod
    def rewrite_user_data():
        WriteFakerCSV.write_csv_file("fakeUsers.csv", FakerUserGenerator(), 500)
        
    @staticmethod
    def rewrite_user_data():
        WriteFakerCSV.write_csv_file("fakeBooks.csv", FakerBookGenerator(), 500)