def calc_imc(p, a):
    return p / (a ** 2)

def interp_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    p = float(input("Digite seu peso em kg: "))
    a = float(input("Digite sua altura em metros: "))

    imc = calc_imc(p, a)
    interpretação = interp_imc(imc)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Interpretação: {interpretação}")

if __name__ == "__main__":
    main()

