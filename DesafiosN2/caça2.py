import math
import os
import random

tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

linha_tabuleiro_diamante = random.randint(0, 2)
coluna_tabuleiro_diamante = random.randint(0, 2)

tentativas = 0


def limpar_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def exibe_tabuleiro():
    print("    0   1   2")
    print("  -------------")

    for i, linha in enumerate(tabuleiro):
        print(f"{i} | " + " | ".join(linha) + " |")
        print("  -------------")


def fazer_jogada(linha, coluna):
    # Valida o range de valores de linha e coluna
    if not (0 <= linha <= 2 and 0 <= coluna <= 2):
        print("Jogada fora dos limites!")
        return [False, tentativas]

    if linha == linha_tabuleiro_diamante and coluna == coluna_tabuleiro_diamante:
        tabuleiro[linha][coluna] = '💎'
        return [True, tentativas]

    tabuleiro[linha][coluna] = 'X'
    return [False, tentativas + 1]


while True:
    limpar_console()
    exibe_tabuleiro()

    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))

        resultado = fazer_jogada(linha, coluna)
        achou_o_diamante = resultado[0]
        tentativas = resultado[1]

        if achou_o_diamante:
            limpar_console()
            exibe_tabuleiro()
            print("Parabéns, você encontrou o Diamante! 💎")
            break
        elif tentativas >= 5:
            print("Que pena, você não encontrou o Diamante! 💎")
            print(f"O Diamante estava na linha {linha_tabuleiro_diamante} e na coluna {coluna_tabuleiro_diamante}")
            tabuleiro[linha_tabuleiro_diamante][coluna_tabuleiro_diamante] = '💎'
            exibe_tabuleiro()
            break

    except IndexError:
        print('Digite valores entre 0 e 2!')
    except ValueError:
        print('Os valores devem ser números inteiros!')
