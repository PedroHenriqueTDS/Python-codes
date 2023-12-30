class Restaurante:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.reservas = []

    def fazer_reserva(self, nome, numero_pessoas):
        if numero_pessoas > self.capacidade:
            print("Desculpe, nao temos capacidade para essa quantidade de pessoas.")
            return False
        elif numero_pessoas + sum([reserva[1] for reserva in self.reservas]) > self.capacidade:
            print("Desculpe, nao temos disponibilidade para essa quantidade no momento.")
            return False
        else:
            self.reservas.append((nome, numero_pessoas))
            print(f"Reserva feita para {nome} para {numero_pessoas} pessoas.")
            return True

    def mostrar_reservas(self):
        print("Reservas Atuais:")
        for reserva in self.reservas:
            print(f"- {reserva[0]}: {reserva[1]} pessoas")

def main():
    restaurante = Restaurante(40) 

    while True:
        print("\n1. Fazer reserva")
        print("2. Mostrar reservas")
        print("3. Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Nome para a reserva: ")
            numero_pessoas = int(input("Numero de pessoas: "))
            restaurante.fazer_reserva(nome, numero_pessoas)
        elif opcao == "2":
            restaurante.mostrar_reservas()
        elif opcao == "3":
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()