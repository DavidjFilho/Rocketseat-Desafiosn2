def olaMundo():
    print('Olá Mundo!')

def olaPessoa(nome):
    print(f'Olá, {nome}!')

# olaPessoa('Filho')

def dobro(numero):
    return numero * 2

#print(dobro(5))

def multiplicacao(a, b = 5):
    """Multiplica dois números"""
    return a * b

#print(multiplicacao(5, 10))
#print(multiplicacao(5))

x = 5 #varial global

def soma():
    x = 10 #varial local
    print(x)
    return x + 1

soma()
print(x)
print(soma())