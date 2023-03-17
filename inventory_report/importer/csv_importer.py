import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def load_data(file):
        data = CsvImporter.csv_format(file)
        return data

    def csv_format(path):
        data = []
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            file_reader = csv.DictReader(file)
            for item in file_reader:
                data.append(item)
        return data
