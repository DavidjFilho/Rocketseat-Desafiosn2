print('Olá, sou sua assistente Sabrina, o que queres fazer hoje?')

comando = input('Digite um comando: ')

match comando:
    case 'oi' | 'Olá':
        print('Oi, como vai você?')
    case 'tchau' | 'exit' | 'fim':
        print('Tchau, foi um prazer')
    case 'piada':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? o São Login')
    case 'clima':
        print('Muito quente!!!')
    case _:
        print('Desculpe, não entendi o comando!')