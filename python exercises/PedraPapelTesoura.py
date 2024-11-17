import random

def jogar():
    jogadas = ["ppedra", "papel", "tesoura", "lagarto", "spock"]

    print("Bem-vindo ao jogo Pedra, Papel, Tesoura, Lagarto, Spock!!!")
    print("As regras são as seguintes:")
    print("Pedra esmaga tesoura;")
    print("Tesoura corta papel,")
    print("Papel cobre pedra.")
    print("Pedra esmaga lagarto.")
    print("Lagarto envenena Spock.")
    print("Spock esmaga tesoura.")
    print("Tesoura decapita lagarto.")
    print("Lagarto come pape")
    print("Papel refuta Spock.")
    print("Spock vaporiza pedra.")

    while True:
        escolhaPlayer = input("Escolha sua jogada: ").lower()
        if escolhaPlayer in jogadas:
            escolhaPC = random.choice(jogadas)

            print(f"Você escolheu: {escolhaPlayer}")
            print(f"O computador escolheu: {escolhaPC}")

            if escolhaPlayer == escolhaPC:
                print("Empate!")
            elif (escolhaPlayer == "pedra" and (escolhaPC == "tesoura" or escolhaPC == "lagarto")) or \
                 (escolhaPlayer == "tesoura" and (escolhaPC == "papel" or escolhaPC == "lagarto")) or \
                 (escolhaPlayer == "papel" and (escolhaPC == "pedra" or escolhaPC == "spock")) or \
                 (escolhaPlayer == "lagarto" and (escolhaPC == "papel" or escolhaPC == "spock")) or \
                 (escolhaPlayer == "spock" and (escolhaPC == "tesoura" or escolhaPC == "pedra")):
                print("Você venceu!")
            else:
                print("O computador venceu!")

            NovoJogo = input("Deseja jogar novamente? (sim/não): ").lower()
            if NovoJogo != "sim":
                print("Obrigado por jogar!")
                break
        else:
            print("Escolha inválida.Por favor, escolha entre pedra, papel, tesoura, lagarto ou spock")

if __name__ == "__main__":
    jogar()
