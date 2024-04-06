import random

def adivinha():
    nSecreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Estou pensando em um número entre 1 e100. Tente adivinhar.")

    while True:
        palpite = int(input("Digite um número: "))
        tentativas += 1

        if palpite < nSecreto:
            print("Tente um número maior.")
        elif palpite > nSecreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    adivinha()
