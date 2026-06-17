from produto import *
from estoque import *
from vendas import *

def menu():

    while True:

        print("""
1 - Cadastrar produto
2 - Consultar estoque
3 - Atualizar estoque
4 - Registrar venda
5 - Relatório de vendas
6 - Remover produto
0 - Sair
""")

        opcao = input("Escolha: ")

        if opcao == "1":
            codigo = input("Código: ")
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            tamanho = input("Tamanho: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            print(
                cadastrar_produto(
                    codigo,
                    nome,
                    categoria,
                    tamanho,
                    preco,
                    quantidade
                )
            )

        elif opcao == "2":
            exibir_estoque()

        elif opcao == "3":
            codigo = input("Código: ")
            quantidade = int(input("Nova quantidade: "))
            print(atualizar_quantidade(codigo, quantidade))

        elif opcao == "4":
            codigo = input("Código: ")
            quantidade = int(input("Quantidade vendida: "))
            print(registrar_venda(codigo, quantidade))

        elif opcao == "5":
            print(relatorio_vendidos())

        elif opcao == "6":
            codigo = input("Código: ")
            print(remover_produto(codigo))

        elif opcao == "0":
            break

menu()
