from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "leite",
        "parmalat",
        "02/02/02",
        "02/03/02",
        1234,
        "manter resfriado",
    )
    assert product.id == 1
    assert product.nome_do_produto == "leite"
    assert product.nome_da_empresa == "parmalat"
    assert product.data_de_fabricacao == "02/02/02"
    assert product.data_de_validade == "02/03/02"
    assert product.numero_de_serie == 1234
    assert product.instrucoes_de_armazenamento == "manter resfriado"
