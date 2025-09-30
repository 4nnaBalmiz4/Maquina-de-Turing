import json
import sys

argvs = sys.argv
arquivo1 = argvs[1]
arquivo2 = argvs[2]
arquivo_saida = argvs[3]

with open(arquivo1, 'r') as dados:
    arq_json = json.load(dados)

estadoInicial = arq_json["initial"]
estadoFinal = arq_json["final"]
branco = arq_json["white"]
transicoes = arq_json["transitions"]

with open(arquivo2, 'r+') as txt:
    entrada = list(txt.read().strip())

    posicao = 0

    while estadoInicial not in estadoFinal:
        if posicao < 0 or posicao >= len(entrada):
            entrada.insert(posicao, branco)
        caractereAtual = entrada[posicao]

        for transicao in transicoes:
            if transicao["from"] == estadoInicial and transicao["read"] == caractereAtual:
                estadoInicial = transicao["to"]

                if "write" in transicao:
                    entrada[posicao] = transicao["write"]

                if transicao["dir"] == "R":
                    posicao += 1
                elif transicao["dir"] == "L":
                    posicao -= 1

                if posicao == len(entrada):
                    entrada.append(branco)
                elif posicao == -1:
                    entrada.insert(0, branco)

                break

    txt.seek(0)
    txt.truncate()
    txt.write(''.join(entrada))

with open(arquivo_saida, 'w') as saida:
    saida.write(''.join(entrada))

if estadoInicial in estadoFinal:
    print("1")
else:
    print("0")
