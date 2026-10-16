def cadastrar_tarefa(tarefas):
    print("\n--- Cadastro de nova tarefa ---")

    while True:
        titulo = input("Título: ").strip()
        if titulo:
            break
        print("Erro: o título é obrigatório. Digite um título válido.")

    descricao = input("Descrição: ").strip()

    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }

    while True:
        prioridade_digitada = input("Prioridade (Alta, Média ou Baixa): ").strip().casefold()
        if prioridade_digitada in prioridades:
            prioridade = prioridades[prioridade_digitada]
            break
        print("Erro: prioridade inválida. Escolha Alta, Média ou Baixa.")

    data_limite = input("Data limite (ex.: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or 'Não informada'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or 'Não informada'}")
        print(f"Status: {tarefa['status']}")


def main():
    tarefas = []

    while True:
        print("\n========== TASKTRACKER ==========")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
