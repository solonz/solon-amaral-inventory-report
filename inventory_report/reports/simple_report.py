from datetime import date, datetime
from collections import Counter


class SimpleReport:
    def __oldest_product(products_list):
        all_dates = [
            product["data_de_fabricacao"] for product in products_list
        ]

        return min(all_dates)

    def __next_expire(products_list):
        dates_from_today = [
            product["data_de_validade"] for product in products_list
            if datetime.strptime(product["data_de_validade"], '%Y-%m-%d')
            .date() >= date.today()
        ]

        return min(dates_from_today)

    def __more_products_company(products_list):
        companies = [
            product["nome_da_empresa"] for product in products_list
        ]
# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
        return Counter(companies).most_common(1)[0][0]

    @staticmethod
    def generate(list):
        oldest_product = SimpleReport.__oldest_product(list)
        next_expire = SimpleReport.__next_expire(list)
        more_products_company = SimpleReport.__more_products_company(list)

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {next_expire}\n"
            f"Empresa com mais produtos: {more_products_company}"
        )
