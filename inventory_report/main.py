import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    # https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
    # https://learnpython.com/blog/python-standard-error-stream/
    # https://www.geeksforgeeks.org/sys-stdout-write-in-python/
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    if sys.argv[1].endswith('csv'):
        inventory = InventoryRefactor(CsvImporter)
        sys.stdout.write(inventory.import_data(sys.argv[1], sys.argv[2]))

    if sys.argv[1].endswith('json'):
        inventory = InventoryRefactor(JsonImporter)
        sys.stdout.write(inventory.import_data(sys.argv[1], sys.argv[2]))

    if sys.argv[1].endswith('xml'):
        inventory = InventoryRefactor(XmlImporter)
        sys.stdout.write(inventory.import_data(sys.argv[1], sys.argv[2]))
