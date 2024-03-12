from pathlib import Path
from fakerData.faker_abs_generator import FakerAbsGenerator

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
           