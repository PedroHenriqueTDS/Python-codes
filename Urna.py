class Eleicao:
    def __init__(self, candidatos):
        self.candidatos = candidatos
        self.votos = {candidato: 0 for candidato in candidatos}

    def votar(self):
        print("Candidatos:")
        for candidato in self.candidatos:
            print(candidato)
        nome_candidato = input("Em quem voce deseja votar? ")
        if nome_candidato in self.candidatos:
            self.votos[nome_candidato] += 1
            print(f"Voto registrado para {nome_candidato}.")
        else:
            print("Candidato nao encontrado.")

    def consultar_votos(self):
        for candidato, voto in self.votos.items():
            print(f"{candidato}: {voto} votos")

    def candidato_ganhando(self):
        ganhador = max(self.votos, key=self.votos.get)
        print(f"Candidato a frente: {ganhador} com {self.votos[ganhador]} votos")

    def resultado_final(self):
        total_votos = sum(self.votos.values())
        print("Resultado Final da Eleicao:")
        for candidato, voto in sorted(self.votos.items(), key=lambda item: item[1], reverse=True):
            percentual = (voto / total_votos) * 100
            print(f"{candidato}: {voto} votos ({percentual:.2f} %)")

def main():
    candidatos = ["Alane", "Pedro", "Clara", "Lucas"]
    eleicao = Eleicao(candidatos)

    while True:
        print("\nMenu:")
        print("1 - Votar")
        print("2 - Consultar numero de votos")
        print("3 - Verificar qual candidato esta ganhando")
        print("4 - Encerrar votacao")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            eleicao.votar()
        elif opcao == "2":
            eleicao.consultar_votos()
        elif opcao == "3":
            eleicao.candidato_ganhando()
        elif opcao == "4":
            eleicao.resultado_final()
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()