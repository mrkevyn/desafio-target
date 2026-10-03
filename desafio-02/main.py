import json
from pathlib import Path

def carregar_estoque():
    caminho = Path(__file__).parent / "estoque.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["estoque"]

def encontrar_produto(estoque, codigo_produto):
    for produto in estoque:
        if produto["codigoProduto"] == codigo_produto:
            return produto

    return None

def realizar_movimentacao(
    estoque,
    identificador,
    codigo_produto,
    tipo_movimentacao,
    quantidade
):
    produto = encontrar_produto(estoque, codigo_produto)

    if produto is None:
        return {
            "sucesso": False,
            "mensagem": "Produto não encontrado."
        }

    if quantidade <= 0:
        return {
            "sucesso": False,
            "mensagem": "A quantidade deve ser maior que zero."
        }

    tipo = tipo_movimentacao.strip().lower()

    if tipo == "entrada":
        produto["estoque"] += quantidade

    elif tipo == "saida":
        if quantidade > produto["estoque"]:
            return {
                "sucesso": False,
                "mensagem": "Estoque insuficiente."
            }

        produto["estoque"] -= quantidade

    else:
        return {
            "sucesso": False,
            "mensagem": "Tipo de movimentação inválido. Use entrada ou saida."
        }

    return {
        "sucesso": True,
        "identificador": identificador,
        "descricao": tipo,
        "produto": produto["descricaoProduto"],
        "quantidade": quantidade,
        "estoqueFinal": produto["estoque"]
    }

def main():
    estoque = carregar_estoque()

    print("MOVIMENTAÇÃO DE ESTOQUE")

    identificador = input("Identificador da movimentação: ")
    codigo = int(input("Código do produto: "))
    tipo = input("Tipo de movimentação (entrada/saida): ")
    quantidade = int(input("Quantidade: "))

    resultado = realizar_movimentacao(
        estoque,
        identificador,
        codigo,
        tipo,
        quantidade
    )

    print("\n RESULTADO")

    if resultado["sucesso"]:
        print(f"ID: {resultado['identificador']}")
        print(f"Movimentação: {resultado['descricao']}")
        print(f"Produto: {resultado['produto']}")
        print(f"Quantidade movimentada: {resultado['quantidade']}")
        print(f"Estoque final: {resultado['estoqueFinal']}")
    else:
        print(f"Erro: {resultado['mensagem']}")

if __name__ == "__main__":
    main()
