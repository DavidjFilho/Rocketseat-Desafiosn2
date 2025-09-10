import os

tasks = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("0 - Sair")


def add_task():
    titulo = input("Digite o título da tarefa: ").strip()
    if not titulo:
        print("Tarefa não pode ser vazia.")
        return
    tasks.append({"titulo": titulo, "concluida": False})
    print("Tarefa adicionada!")


def list_tasks():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nTarefas:")
    for index, task in enumerate(tasks, start=1):
        status = "Concluída" if task["concluida"] else "Pendente"
        print(f"{index}. [{status}] {task['titulo']}")


def complete_task():
    if not tasks:
        print("Nenhuma tarefa para concluir.")
        return
    list_tasks()
    entrada = input("Informe o número da tarefa a concluir: ")
    if not entrada.isdigit():
        print("Digite um número válido.")
        return
    idx = int(entrada)
    if idx < 1 or idx > len(tasks):
        print("Número fora do intervalo.")
        return
    tasks[idx - 1]["concluida"] = True
    print("Tarefa marcada como concluída!")


def remove_task():
    if not tasks:
        print("Nenhuma tarefa para remover.")
        return
    list_tasks()
    entrada = input("Informe o número da tarefa a remover: ")
    if not entrada.isdigit():
        print("Digite um número válido.")
        return
    idx = int(entrada)
    if idx < 1 or idx > len(tasks):
        print("Número fora do intervalo.")
        return
    removida = tasks.pop(idx - 1)
    print(f"Tarefa removida: {removida['titulo']}")


def main():
    while True:
        clear_screen()
        show_menu()
        opcao = input("Escolha uma opção: ")
        if not opcao.isdigit():
            print("Opção inválida. Digite um número.")
            input("Pressione Enter para continuar...")
            continue
        opcao = int(opcao)

        if opcao == 1:
            add_task()
        elif opcao == 2:
            list_tasks()
        elif opcao == 3:
            complete_task()
        elif opcao == 4:
            remove_task()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()


