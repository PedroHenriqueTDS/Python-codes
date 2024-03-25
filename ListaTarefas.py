class GerenciadorTarefas:
    def __init__(self):
        self.lista_tarefas = []

    def adicionar_tarefa(self, nova_tarefa):
        self.lista_tarefas.append({"tarefa": nova_tarefa, "concluida": False})
        print("Tarefa adicionada com sucesso!")

    def excluir_tarefa(self, indice):
        try:
            tarefa_removida = self.lista_tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
        except IndexError:
            print("Índice inválido!")

    def listar_tarefas(self):
        if self.lista_tarefas:
            print("Lista de tarefas:")
            for indice, tarefa in enumerate(self.lista_tarefas):
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                print(f"{indice + 1}. {tarefa['tarefa']} - {status}")
        else:
            print("Não há tarefas na lista.")

    def marcar_tarefa_concluida(self, indice):
        try:
            self.lista_tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída.")
        except IndexError:
            print("Índice inválido!")

    def salvar_tarefas(self, nome_arquivo="tarefas.txt"):
        with open(nome_arquivo, "w") as arquivo:
            for tarefa in self.lista_tarefas:
                arquivo.write(f"{tarefa['tarefa']},{tarefa['concluida']}\n")

    def carregar_tarefas(self, nome_arquivo="tarefas.txt"):
        try:
            with open(nome_arquivo, "r") as arquivo:
                for linha in arquivo:
                    tarefa, concluida = linha.strip().split(",")
                    self.lista_tarefas.append({"tarefa": tarefa, "concluida": concluida == "True"})
            print("Tarefas carregadas com sucesso!")
        except FileNotFoundError:
            print("Arquivo de tarefas não encontrado.")

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.carregar_tarefas()

    while True:
        print("\nEscolha uma opção:")
        print("1. ➕Adicionar tarefa➕")
        print("2. ❌Excluir tarefa❌")
        print("3. 📝Listar tarefas📝")
        print("4. ✅Marcar tarefa como concluída✅")
        print("5. 💾Salvar tarefas💾")
        print("6. 🚪Sair🚪")

        opcao = input("👉👉 ")

        if opcao == "1":
            nova_tarefa = input("Digite a nova tarefa: ")
            gerenciador.adicionar_tarefa(nova_tarefa)
        elif opcao == "2":
            gerenciador.listar_tarefas()
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            gerenciador.excluir_tarefa(indice)
        elif opcao == "3":
            gerenciador.listar_tarefas()
        elif opcao == "4":
            gerenciador.listar_tarefas()
            indice = int(input("Digite o índice da tarefa concluída: ")) - 1
            gerenciador.marcar_tarefa_concluida(indice)
        elif opcao == "5":
            gerenciador.salvar_tarefas()
            print("Tarefas salvas com sucesso!")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
