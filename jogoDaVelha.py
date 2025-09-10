tabuleiro = [
    [' ', ' ', ' '], 
    [' ', ' ', ' '], 
    [' ', ' ', ' ']
]

jogador = 'X'

def exibirTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or 
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada inválida!')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'

def temGanhador():
    """"Verifica as linhas"""
    for linha in range (3):
        if(
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro [linha][1] and
            tabuleiro[linha][0] == tabuleiro [linha][2]
        ):
            print(f'{tabuleiro[linha][0]} Ganhou!!!')
            return True

    """Verifica as colunas"""
    for coluna in range (3):
        if(
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro [1][coluna] and
            tabuleiro[0][coluna] == tabuleiro [2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} Ganhou!!!')
            return True
    """ Verifica as diagonais"""
    if (
       tabuleiro[1][1] != ' ' and 
       (
            (
                tabuleiro[0][0] == tabuleiro [1][1] and
                tabuleiro[0][0] == tabuleiro [2][2]
            ) or
            (
                tabuleiro[0][2] == tabuleiro [1][1] and
                tabuleiro[1][1] == tabuleiro [2][0]
            )
       )
    ):
        print(f'{tabuleiro[1][1]} Ganhou!!!')
        return True
    
    """ Se não teve ganhador em nenhuma forma """
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('Empate')
    return True

while True:
    print(f'Jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except IndexError:
        print('Digite valores números entre 0 e 2!')
    except ValueError:
        print('Os valores devem ser números inteiros!')
    exibirTabuleiro()
    if temGanhador() or temEmpate():
        break
    