# Validador de Bandeiras

Este projeto identifica a bandeira ("Bandeira") de um cartão de crédito a partir do número informado, utilizando regras de prefixo (IIN) e comprimento do cartão.

## Funcionalidades

- Detecta as principais bandeiras de cartões:
  - Visa
  - Visa Electron
  - MasterCard
  - American Express
  - Diners Club (Carte Blanche e International)
- Fácil de usar e expandir.

## Como usar

1. Clone ou baixe este repositório.
2. Execute o arquivo `main.py` ou importe a função `get_card_brand` em seu projeto.

### Exemplo de uso

```python
from main import get_card_brand

numero = "4111 1111 1111 1111"
bandeira = get_card_brand(numero)
print(bandeira)  # Saída: Visa
```

Ou execute diretamente:

```bash
python main.py
```

## Exemplo de saída

```
3013 366228 2626: Diners Club - Carte Blanche
```

## Estrutura do Projeto

```
Validador_de_Bandeiras/
│
├── main.py        # Código Python para validação
├── README.md      # Este arquivo
└── cards band.png # Imagem de referência das bandeiras (se aplicável)
```

## Licença

Este projeto está sob a licença MIT.
