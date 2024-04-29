import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    while True:
        try:
            comprimento = int(input("Digite a quantidade de caracteres da senha desejada: "))
            if comprimento <= 0:
                print("Por favor, digite um número inteiro positivo maior que zero.")
            else:
                senha = gerar_senha(comprimento)
                print("Sua senha gerada é:", senha)
                break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
