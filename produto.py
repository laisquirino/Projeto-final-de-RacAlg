from persistencia import carregar

estoque = carregar()

def cadastrar_produto(codigo, nome, categoria, tamanho, preco, quantidade):
    if codigo in estoque:
        return "Produto já cadastrado."

    estoque[codigo] = {
        "nome": nome,
        "categoria": categoria,
        "tamanho": tamanho,
        "preco": float(preco),
        "quantidade": int(quantidade),
        "vendidos": 0
    }

    return "Produto cadastrado com sucesso."


def remover_produto(codigo):
    if codigo not in estoque:
        return "Produto não encontrado."

    estoque.pop(codigo)
    return "Produto removido."


def consultar_produto(codigo):
    if codigo not in estoque:
        return None

    return estoque[codigo]
