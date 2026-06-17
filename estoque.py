from produto import estoque

def consultar_estoque():
    return estoque


def atualizar_quantidade(codigo, nova_quantidade):
    if codigo not in estoque:
        return "Produto não encontrado."

    estoque[codigo]["quantidade"] = nova_quantidade

    return "Quantidade atualizada."


def exibir_estoque():
    if not estoque:
        print("Estoque vazio.")
        return

    for codigo, produto in estoque.items():
        print(
            codigo,
            produto["nome"],
            produto["quantidade"]
        )
