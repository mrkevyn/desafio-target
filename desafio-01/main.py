import json
from pathlib import Path

def calcular_comissao(valor):
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05

def calcular_comissoes(vendas):
    comissoes = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        comissao = calcular_comissao(valor)

        comissoes[vendedor] = comissoes.get(vendedor, 0) + comissao

    return comissoes

def main():
    caminho = Path(__file__).parent / "vendas.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    comissoes = calcular_comissoes(dados["vendas"])

    print("COMISSÕES POR VENDEDOR")

    for vendedor, comissao in comissoes.items():
        print(f"{vendedor}: R$ {comissao:.2f}")


if __name__ == "__main__":
    main()
