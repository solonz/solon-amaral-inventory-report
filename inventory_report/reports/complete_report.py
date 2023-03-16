from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    simple_report = SimpleReport()

    @staticmethod
    def companiesProducts(products_list):
        companies = [
            product["nome_da_empresa"] for product in products_list
            ]

        companies_qty = Counter(companies)
        stock_report = ""
        for company in companies_qty:
            stock_report += f"- {company}: {companies_qty[company]}\n"

        return stock_report

    @staticmethod
    def generate(products_list):
        simple_report = SimpleReport.generate(products_list)
        companies_products = CompleteReport.companiesProducts(products_list)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_products}\n"
        )
