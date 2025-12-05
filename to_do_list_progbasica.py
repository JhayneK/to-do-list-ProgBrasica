tarefas = []

def adicionar_tarefa():
    # Input do usuário para nova tarefa
    descricao = input("Digite a nova tarefa: ")
    # Cria um dicionário da tarefa
    tarefa = {
        "descricao": descricao,  
        "concluida": False       
    }
    # Adiciona a tarefa a uma lista de tarefas
    tarefas.append(tarefa)
    # Confirma para o usuário com uma mensagem em tela
    print(f"Tarefa adicionada: {descricao}")

def listar_tarefas():
    # Caso não haja nenhuma tarefa na lista
    if not tarefas:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        print("\nSuas tarefas:")
        # Percorre a lista de tarefas com índice
        for i, tarefa in enumerate(tarefas, start=1):
            # Marcador para mostrar se a tarefa está concluída ou não "[X]" para concluída, "[ ]" para pendente
            status = "[X]" if tarefa["concluida"] else "[ ]"
            # Mostrar número, status e descrição da tarefa
            print(f"{i}. {status} {tarefa['descricao']}")
        print()

def marcar_tarefa_concluida():
    # Printa em tela os índices das tarefas para o usuário 
    listar_tarefas()

    # Se não tiver tarefas, retorna
    if not tarefas:
        return

    # Pede o número da tarefa a ser marcada como concluída
    numero = input("Digite o número da tarefa que deseja marcar como concluída: ")

    # Verifica se o que foi digitado é um número
    if not numero.isdigit():
        print("Você precisa digitar um número válido.")
        return

    # Converte o texto para inteiro
    indice = int(numero) - 1  

    # Verifica se o número está dentro do intervalo de tarefas existentes
    if 0 <= indice < len(tarefas):
        # Marca a tarefa como concluída
        tarefas[indice]["concluida"] = True
        # Mostra qual tarefa foi marcada
        print(f"Tarefa concluída: {tarefas[indice]['descricao']}")
    else:
        # Se o número não corresponde a nenhuma tarefa
        print("Número de tarefa inválido.")

def remover_tarefa():
    # Mostramos as tarefas atuais
    listar_tarefas()

    # Se não tiver tarefas, não há o que remover
    if not tarefas:
        return

    # Pede o número da tarefa a ser removida
    numero = input("Digite o número da tarefa que deseja remover: ")

    # Verifica se o que foi digitado é um número
    if not numero.isdigit():
        print("Você precisa digitar um número válido.")
        return

    # Converte o texto para inteiro
    indice = int(numero) - 1 

    # Verifica se o índice é válido
    if 0 <= indice < len(tarefas):
        # Guarda a tarefa removida só para mostrar na mensagem
        tarefa_removida = tarefas.pop(indice)  # remove e retorna a tarefa
        print(f"Tarefa removida: {tarefa_removida['descricao']}")
    else:
        print("Número de tarefa inválido.")

def menu():
    # Loop infinito até o usuário escolher sair
    while True:
        print("=== TO-DO LIST ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefa como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")

        # Pede a opção do usuário
        opcao = input("Escolha uma opção: ")

        # Verifica qual opção foi escolhida e chama a função correspondente
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_tarefa_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")
        print("-" * 30)

# Garante que o menu só seja chamado se o arquivo for executado diretamente
if __name__ == "__main__":
    menu()
