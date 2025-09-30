# Implementação de Automato Finito 

Este projeto implementa uma Maquina de Turing em Python, contendo um arquivo com um diagrama de transição e um arquivo com entrada teste, estes são combinados e excutados, resultando em um arquivo de saída. 

## Tecnologias Utilizadas

- **Python** - Linguagem principal do projeto
- **JSON** - Especificação da Máquina de Estados
- **txt** - Entradas para Teste e Saída

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- `Turing.py` - Arquivo principal 
- `duplo_bal.json` - Especificações do autômato
- `duplobal.in.txt` - Arquivo de entrada
- `duplobal2.in.txt` - Arquivo de entrada
- `duplobal3.in.txt` - Arquivo de entrada
- `fitaFinal1.txt` - Arquivo de Saída
- `fitaFinal3.txt` - Arquivo de Saída

## Como Executar

1. **Baixe e instale o Python**, caso ainda não tenha:
     
2. **Execute o simulador**:
   ```sh
   python Turing.py duplo_bal.json duplobal.in.txt fitaFinal1.txt
   ```

O simulador irá processar o arquivo `Turing.py`, verificar as especificações do arquivo txt `duplobal.in.txt`, e então executar o código, o que resultará em um arquivo de saída txt `fitaFinal1.txt`.

## Exemplo de JSON (`input.lang`)

```c
{
    "initial" : 0,
    "final" : [4],
    "white" : "_",
    "transitions" : [
        {"from": 0, "to": 1, "read": "a", "write": "A", "dir":"R"},
        {"from": 1, "to": 1, "read": "a", "write": "a", "dir":"R"},
        {"from": 1, "to": 1, "read": "B", "write": "B", "dir":"R"},
        {"from": 1, "to": 2, "read": "b", "write": "B", "dir":"L"},
        {"from": 2, "to": 2, "read": "B", "write": "B", "dir":"L"},
        {"from": 2, "to": 2, "read": "a", "write": "a", "dir":"L"},
        {"from": 2, "to": 0, "read": "A", "write": "A", "dir":"R"},
        {"from": 0, "to": 3, "read": "B", "write": "B", "dir":"R"},
        {"from": 3, "to": 3, "read": "B", "write": "B", "dir":"R"},
        {"from": 3, "to": 4, "read": "_", "write": "_", "dir":"L"}      
    ]
}
```

Exemplo de Entrada:
```
aabb
```

Saída esperada(Arquivo):
```
AABB_
```

Saída esperada(Linha de Comando):
```
1
```

## Aluna
* Anna Laura Balmiza Soares
