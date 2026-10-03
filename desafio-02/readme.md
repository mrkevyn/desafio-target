# Desafio 02 — Movimentação de Estoque

Programa desenvolvido em Python para realizar uma movimentação de entrada ou saída de produtos em estoque, utilizando os dados fornecidos em um arquivo JSON.

## Funcionalidades

O programa permite informar:

* Identificador da movimentação;
* Código do produto;
* Tipo da movimentação (`entrada` ou `saida`);
* Quantidade movimentada.

Após a movimentação, o programa apresenta o estoque final do produto.

## Regras

### Entrada

Uma movimentação do tipo `entrada` adiciona a quantidade informada ao estoque atual.

### Saída

Uma movimentação do tipo `saida` reduz a quantidade informada do estoque.

O programa não permite realizar uma saída maior que o estoque disponível.

### Validações

O programa também verifica:

* Se o produto informado existe;
* Se a quantidade é maior que zero;
* Se o tipo de movimentação é válido;
* Se existe estoque suficiente para uma saída.

## Estrutura

```text
desafio-02/
├── main.py
├── estoque.json
└── README.md
```

### `main.py`

Contém a implementação da lógica de movimentação de estoque.

### `estoque.json`

Contém os produtos e seus respectivos estoques iniciais utilizados pelo programa.

## Tecnologias

* Python 3
* JSON
* `pathlib`
* Bibliotecas padrão do Python

## Como executar

Certifique-se de ter o Python 3 instalado.

No terminal, dentro da pasta `desafio-02`, execute:

```bash
python main.py
```

## Exemplo de execução

```text
MOVIMENTAÇÃO DE ESTOQUE

Identificador da movimentação: 1
Código do produto: 101
Tipo de movimentação (entrada/saida): entrada
Quantidade: 50

RESULTADO
ID: 1
Movimentação: entrada
Produto: Caneta Azul
Quantidade movimentada: 50
Estoque final: 200
```

Considerando que a quantidade inicial da **Caneta Azul** seja 150 unidades, após uma entrada de 50 unidades o estoque final será de 200 unidades.

## Observação

O arquivo `estoque.json` é utilizado como fonte dos dados iniciais. As alterações realizadas durante a execução são mantidas apenas em memória e não alteram o arquivo JSON.
