# Sistema de Gerenciamento de Mercado

Projeto simples em **Python** que simula um sistema de gerenciamento de um mercado com acesso para **gerente** e **cliente**.

## Funcionalidades

### Menu do Gerente
- Adicionar produto
- Remover produto
- Atualizar informações de produto
- Visualizar produtos
- Visualizar funcionários

O acesso ao menu do gerente é protegido por **senha**.

### Menu do Cliente
- Visualizar produtos
- Adicionar produtos ao **carrinho de compras**
- Calcular **total da compra**

## Estrutura do Sistema

O sistema utiliza:

- **Dicionário de produtos** contendo:
  - nome
  - preço
  - quantidade em estoque

- **Lista de funcionários** do mercado

- **Carrinho de compras** para registrar produtos escolhidos pelo cliente

## Recursos utilizados

- Funções
- Dicionários
- Listas
- Estrutura `match case`
- Tratamento de erros (`try/except`)
- Validação de entrada de dados

