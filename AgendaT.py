def CarregarAgenda():
    try:
        with open("agenda.txt", "r") as arquivo:
            for linha in arquivo:
                nome, telefone = linha.strip().split(":")
                agenda[nome] = telefone
    except FileNotFoundError:
        print("⚠️ Arquivo da agenda não encontrado. Uma nova agenda será criada.")

def salvar():
    with open("agenda.txt", "w") as arquivo:
        for nome, telefone in agenda.items():
            arquivo.write(f"{nome}:{telefone}\n")

agenda = {}

def adicionar(nome, telefone):
    if nome not in agenda:
        agenda[nome] = telefone
        print("✅ Contato adicionado com sucesso!")
    else:
        print("📌 Este contato jáexiste na agenda.")

def remover(nome):
    if nome in agenda:
        del agenda[nome]
        print("🗑️ Contato removido com sucesso!")
    else:
        print("🚫Este contato não existe na agenda.")

def buscar(nome):
    if nome in agenda:
        print(f"🔍 Nome: {nome}, Telefone: {agenda[nome]}")
    else:
        print("🔒 Contato não encontrado na agenda.")

def listar():
    if agenda:
        print("📋 Lista de Contatos:")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("📌 A agenda está vazia.")

def menu():
    print("\n=== Agenda Telefônica ===")
    print("1.Adicionar Contato")
    print("2. Remover Contato")
    print("3. Buscar Contato")
    print("4. Listar Contatos")
    print("5. Salvar Agenda")
    print("6. Sair")

CarregarAgenda()

while True:
    menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite  o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar(nome, telefone)

    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja remover: ")
        remover(nome)

    elif opcao == "3":
        nome = input("Digite o nome do contato que deseja buscar: ")
        buscar(nome)

    elif opcao == "4":
        listar()

    elif opcao == "5":
        salvar()
        print("📌 Agenda salva com sucesso!")

    elif opcao == "6":
        print("📌 Salvando agenda e saindo...")
        salvar()
        print("👋 Até logo!")
        break

    else:
        print("❌ Opção inválida. Por favor, escolha uma opção válida.")
