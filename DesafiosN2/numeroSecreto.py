numeroSecreto = 9

tentativas = 0

while True:
    chute = int(input('Adivinhe o número secreto entre 1 e 10: '))
    tentativas += 1
    if chute == numeroSecreto:
        print(f'Você acertou o número secreto em {tentativas} tentativas!')
        break
    else:
        print('Você errou! Tente novamente!')