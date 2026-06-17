from produto import estoque

def registrar_venda(codigo, quantidade):
    if codigo not in estoque:
        return "Produto não encontrado."

    if estoque[codigo]["quantidade"] < quantidade:
        return "Estoque insuficiente."

    estoque[codigo]["quantidade"] -= quantidade
    estoque[codigo]["vendidos"] += quantidade

    total = quantidade * estoque[codigo]["preco"]

    return f"Venda realizada. Total: R$ {total:.2f}"


def relatorio_vendidos():
    relatorio = []

    for codigo, produto in estoque.items():
        relatorio.append({
            "codigo": codigo,
            "nome": produto["nome"],
            "vendidos": produto["vendidos"]
        })

    return relatorio
