USER_DADOS = {
    "nome": "Fulano de Tal",
    "email": "fulano@example.com",
    "idade": 28,
    "cidade": "São Paulo",
}

BANCO_DADOS = {
    "agencia": "0001",
    "conta": "123456-7",
    "moeda": "BRL",
    "saldo": 1520.75,
}

def show_menu():
    print("Escolha uma opção:")
    print("1 - Meus dados pessoais")
    print("2 - Saldo bancário")
    print("3 - Extrato")
    print("4 - Ajuda")
    print("0 - Sair")


def handle_choice(choice: int) -> bool:
    """Executa a ação para a opção escolhida.

    Retorna False para encerrar o programa, True para continuar.
    """
    if choice == 1:
        print("\nDados Pessoais:")
        print(f"Nome: {USER_DADOS['nome']}")
        print(f"Email: {USER_DADOS['email']}")
        print(f"Idade: {USER_DADOS['idade']}")
        print(f"Cidade: {USER_DADOS['cidade']}\n")
    elif choice == 2:
        print("\nInformações Bancárias:")
        print(f"Agência: {BANCO_DADOS['agencia']}")
        print(f"Conta: {BANCO_DADOS['conta']}")
        print(f"Moeda: {BANCO_DADOS['moeda']}")
        print(f"Saldo: {BANCO_DADOS['saldo']:.2f}\n")
    elif choice == 3:
        print("\nExtrato\n")
    elif choice == 4:
        print("\nAjuda: escolha um número correspondente à ação desejada.\n")
    elif choice == 0:
        print("Saindo...")
        return False
    else:
        print("\nOpção inválida. Tente novamente.\n")
    return True


def main():
    continuar = True
    while continuar:
        show_menu()
        entrada = input("Digite o número da opção: ")
        try:
            numero = int(entrada)
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
            continue

        continuar = handle_choice(numero)


if __name__ == "__main__":
    main()


