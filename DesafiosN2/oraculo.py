print('Bem-vindo ao Oráculo da Sagredade, faça sua pergunta!')

pergunta = input('Você quer saber sobre (funções, loops, variáveis, listas)?')

match pergunta:
    case 'funções | funcoes | funcao':
        print('Funções são blocos de código que podem ser chamados em qualquer lugar do programa.')
    case 'loops':
        print('Loops são estruturas de repetição que permitem executar um bloco de código várias vezes.')
    case 'variáveis':
        print('Variáveis são espaços na memória do computador que podem armazenar valores.')
    case 'listas':
        print('Listas são estruturas de dados que podem armazenar vários valores em uma única variável.')
    case _:
        print('Desculpe, não entendi a pergunta!')