import csv
import json
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                data_reader = csv.reader(file, delimiter=",", quotechar='"')
            elif path.endswith(".json"):
                data_content = file.read()
                data_reader = json.loads(data_content())

            # Usando o conceito de desempacotamento
            header, *data = data_reader

        products_list = []
        for product in data:
            products_list.append(dict(zip(header, product)))

        if type == "simples":
            return SimpleReport.generate(products_list)
        elif type == "completo":
            return CompleteReport.generate(products_list)
        else:
            raise Exception("Report Type Not Found!")
