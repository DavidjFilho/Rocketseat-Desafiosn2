tabuleiro = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

linha_tabuleiro = 1
coluna_tabuleiro = 2

def exibe_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

tentativas = 0

print("🚀 Caça ao Tesouro Espacial")
print("Encontre o 💎 escondido no tabuleiro 3x3.")
print("Use números de 0 a 2 para linha e coluna.")
print("Exemplo: linha 1, coluna 2")


for tentativa in range(tentativas):
    linha = int(input(f'Digite a linha de 0 a 2: '))
    coluna = int(input(f'Digite a coluna de 0 a 2: '))

    if linha <= 0 or linha >= 2 or coluna <= 0 or coluna >= 2:
        print('❌ Posição inválida! Tente valores entre 0 e 2.')
        continue

    if linha == linha_tabuleiro and coluna == coluna_tabuleiro:
        tabuleiro[linha][coluna] = '💎'
        print('\n🎉 Você encontrou o 💎!')
        exibe_tabuleiro()
        break
    else:
        if tabuleiro[linha][coluna] != ' ':
            print('⚠️  Essa posição já foi tentada! Tente outra.')
        else:
            tabuleiro[linha][coluna] = 'X'
            print('Nada aqui... continue procurando!')
        exibe_tabuleiro()
else:
    print('\n🚨 Suas tentativas acabaram! Você perdeu!')
    tabuleiro[linha_tabuleiro][coluna_tabuleiro] = '💎'
    exibe_tabuleiro()
    print(f'O tesouro estava em ({linha_tabuleiro}, {coluna_tabuleiro})')
    exibe_tabuleiro()