from datetime import date, datetime

TAXA_DIARIA = 0.025

def calcular_juros(valor, data_vencimento):
    hoje = date.today()

    if data_vencimento >= hoje:
        return 0, 0, valor

    dias_atraso = (hoje - data_vencimento).days

    juros = valor * TAXA_DIARIA * dias_atraso
    valor_atualizado = valor + juros

    return dias_atraso, juros, valor_atualizado

def main():
    print("CALCULADORA DE JUROS")

    valor = float(
        input("Digite o valor da dívida: R$ ").replace(",", ".")
    )

    data_texto = input(
        "Digite a data de vencimento (DD/MM/AAAA): "
    )

    data_vencimento = datetime.strptime(
        data_texto,
        "%d/%m/%Y"
    ).date()

    dias_atraso, juros, valor_atualizado = calcular_juros(
        valor,
        data_vencimento
    )

    print("\n RESULTADO")

    print(f"Valor original: R$ {valor:.2f}")
    print(f"Data de vencimento: {data_vencimento.strftime('%d/%m/%Y')}")
    print(f"Data atual: {date.today().strftime('%d/%m/%Y')}")
    print(f"Dias de atraso: {dias_atraso}")
    print(f"Juros: R$ {juros:.2f}")
    print(f"Valor atualizado: R$ {valor_atualizado:.2f}")

if __name__ == "__main__":
    main()
