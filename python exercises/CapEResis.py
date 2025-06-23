def capEq(capacitors, connection_type):
    if connection_type == "serie":
        return 1 / sum(1 / c for c in capacitors)
    elif connection_type == "paralelo":
        return sum(capacitors)

def resEq(resistors, connection_type):
    if connection_type == "serie":
        return sum(resistors)
    elif connection_type == "paralelo":
        return 1 / sum(1 / r for r in resistors)

def calcCorrenteTensao(resistors, tensao, connection_type):
    if connection_type == "serie":
        i_total = tensao / sum(resistors)
        v = [i_total * r for r in resistors]
        i = [i_total for _ in resistors]
    elif connection_type == "paralelo":
        v = [tensao for _ in resistors]
        i = [tensao / r for r in resistors]
    return i, v

def calcCarga(eletrons):
    CARGA_ELETRON = 1.6e-19
    return eletrons * CARGA_ELETRON

def calcCap(carga, tensao):
    return carga / tensao

def tensoesSerie(carga, capacitors):
    return [carga / c for c in capacitors]

def main():
    while True:
        print("\n=== O que você quer calcular ? ===")
        escolha = input("Capacitores ou Resistores? ").strip().lower()

        if escolha == "capacitores":
            tipo = input("Série ou Paralelo? ").strip().lower()
            qtd = int(input("Quantos capacitores você tem? "))
            tensao = float(input("Tensão da fonte (em volts): "))
            capacitors = []

            if tipo == "paralelo":
                for i in range(qtd):
                    cap = float(input(f"Informe a capacitância do capacitor {i+1} (F): "))
                    capacitors.append(cap)

                print("\nTensão em cada capacitor (paralelo):")
                for i in range(qtd):
                    print(f"Capacitor {i+1}: {tensao:.2f} V")

            elif tipo == "serie":
                for i in range(qtd):
                    cap = float(input(f"Informe a capacitância do capacitor {i+1} (F): "))
                    capacitors.append(cap)

                capEqRes = capEq(capacitors, "serie")
                carga_total = capEqRes * tensao

                print("\nTensão em cada capacitor(série):")
                tensoes = tensoesSerie(carga_total, capacitors)
                for i, tensao_individual in enumerate(tensoes):
                    print(f"Capacitor {i+1}: Tensão = {tensao_individual:.2f} V")

            capEqRes = capEq(capacitors, tipo)
            print("\n===== Resumo dos Resultados =====")
            print(f"Capacitância Equivalente ({tipo}): {capEqRes:.2e} F")
            if tipo == "serie":
                print(f"Carga Total: {carga_total:.2e} C")

        elif escolha == "resistores":
            tipo = input("Série ou Paralelo? ").strip().lower()
            qtd = int(input("Quantos resistores você tem? "))
            tensao = float(input("Tensão da fonte (em volts): "))
            resistors = [float(input(f"Resistor {i+1} (Ω): ")) for i in range(qtd)]

            resEqRes = resEq(resistors, tipo)
            i, v = calcCorrenteTensao(resistors, tensao, tipo)

            print("\n===== Resumo dos Resultados =====")
            print(f"Resistência Equivalente ({tipo}): {resEqRes:.2f} Ω")
            print(f"Corrente Total: {sum(i):.2f} A" if tipo == "paralelo" else f"Corrente Total: {i[0]:.2f} A")

            for idx in range(qtd):
                print(f"Resistor {idx+1}: Corrente = {i[idx]:.2f} A, Tensão = {v[idx]:.2f} V")
        else:
            print("Opção inválida! Porfavor, escolha entre 'capacitores' ou 'resistores'.")
            continue

        repetir = input("\nQuer calcular mais alguma coisa? (s/n): ").strip().lower()
        if repetir != 's':
            print("Tudo bem, até a próxima!")
            break

main()
