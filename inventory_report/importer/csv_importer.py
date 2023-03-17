import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def load_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        else:
            data = CsvImporter.csv_format(path)
            return data

    def csv_format(path):
        with open(path) as file:
            read_csv = csv.DictReader(file, delimiter=",", quotechar='"')
            return [row for row in read_csv]
