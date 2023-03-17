

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, type):

        if path.endswith(".csv"):
            data = CsvImporter.load_data(path)

        elif path.endswith(".json"):
            data = JsonImporter.load_data(path)

        elif path.endswith(".xml"):
            data = XmlImporter.load_data(path)

        else:
            raise ValueError("Formato de arquivo inválido")

        return Inventory.generate(data, type)

    @staticmethod
    def generate(data, type):
        if type == "simples":
            return SimpleReport().generate(data)
        elif type == "completo":
            return CompleteReport().generate(data)
        else:
            raise ValueError("Report Type Not Found!")
