

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def read_file(path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)

        elif path.endswith(".json"):
            return JsonImporter.import_data(path)

        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)

        else:
            raise ValueError("Formato de arquivo inválido")

    @staticmethod
    def import_data(path, type):

        file = Inventory.read_file(path)

        if type == "simples":
            return SimpleReport.generate(file)
        elif type == "completo":
            return CompleteReport.generate(file)
        else:
            raise ValueError("Report Type Not Found!")
