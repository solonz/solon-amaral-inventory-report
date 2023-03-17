from inventory_report.importer.importer import Importer
# https://trybecourse.slack.com/archives/C02TH6V3MC5/p1671143681262509
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def load_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        # https://docs.python-guide.org/scenarios/xml/#:~:text=xmltodict,feel%20like%20working%20with%20JSON.&text=xmltodict%20also%20lets%20you%20roundtrip,memory%2C%20and%20supports%20XML%20namespaces.
        with open(path) as file:
            file_reader = file.read()
            data = xmltodict.parse(file_reader)["dataset"]["record"]
        return data
