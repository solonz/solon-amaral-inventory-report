from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():
    @staticmethod
    def generate(products_list):
        companies = [
            product["nome_da_empresa"] for product in products_list
            ]

        companies_qty = Counter(companies)
        stock_report = ""
        for company in companies_qty:
            stock_report += f"- {company}: {companies_qty[company]}\n"

        return (
            f"{SimpleReport.generate(products_list)}\n"
            f"Produtos estocados por empresa:\n"
            f"{stock_report}"
            )
