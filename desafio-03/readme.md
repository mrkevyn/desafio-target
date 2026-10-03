# Desafio 03 — Calculadora de Juros

Programa desenvolvido em Python para calcular os juros de uma dívida com base no valor informado, na data de vencimento e na quantidade de dias em atraso.

## Funcionalidades

O programa solicita:

* Valor da dívida;
* Data de vencimento no formato `DD/MM/AAAA`.

A partir dessas informações, calcula automaticamente:

* Quantidade de dias em atraso;
* Valor dos juros;
* Valor atualizado da dívida.

## Regra de cálculo

A taxa de juros utilizada é de **2,5% ao dia** sobre o valor original da dívida.

A fórmula utilizada é:

```text
Juros = Valor × 2,5% × Dias de atraso
```

O valor atualizado é calculado da seguinte forma:

```text
Valor atualizado = Valor original + Juros
```

Caso a data de vencimento seja igual ou posterior à data atual, não são aplicados juros.

## Exemplo

Para uma dívida de `R$ 1.000,00` com 4 dias de atraso:

```text
Juros = 1000 × 0,025 × 4
Juros = R$ 100,00
```

Portanto:

```text
Valor original: R$ 1.000,00
Juros: R$ 100,00
Valor atualizado: R$ 1.100,00
```

## Estrutura

```text
desafio-03/
├── main.py
└── README.md
```

### `main.py`

Contém a implementação do cálculo dos juros e a interação com o usuário.

## Tecnologias

* Python 3
* `datetime`
* Bibliotecas padrão do Python

## Como executar

Certifique-se de ter o Python 3 instalado.

No terminal, dentro da pasta `desafio-03`, execute:

```bash
python main.py
```

## Exemplo de execução

```text
CALCULADORA DE JUROS

Digite o valor da dívida: R$ 1000
Digite a data de vencimento (DD/MM/AAAA): 29/09/2026

RESULTADO

Valor original: R$ 1000.00
Data de vencimento: 29/09/2026
Data atual: 03/10/2026
Dias de atraso: 4
Juros: R$ 100.00
Valor atualizado: R$ 1100.00
```

## Observação

O cálculo considera juros simples de 2,5% ao dia sobre o valor original da dívida. A quantidade de dias de atraso é calculada automaticamente utilizando a data atual do sistema.
