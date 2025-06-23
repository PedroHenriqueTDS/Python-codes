def calc_capac(val_capac, tipo_cfg):
    if tipo_cfg == "serie":
        return 1 / sum(1 / c for c in val_capac)
    elif tipo_cfg == "paralelo":
        return sum(val_capac)

def calc_resist(val_resist, tipo_cfg):
    if tipo_cfg == "serie":
        return sum(val_resist)
    elif tipo_cfg == "paralelo":
        return 1 / sum(1 / r for r in val_resist)

def calc_corr_tens(val_resist, tens_fonte, tipo_cfg):
    if tipo_cfg == "serie":
        corr_total = tens_fonte / sum(val_resist)
        tens_resist = [corr_total * r for r in val_resist]
        corr_resist = [corr_total for _ in val_resist]
    elif tipo_cfg == "paralelo":
        tens_resist = [tens_fonte for _ in val_resist]
        corr_resist = [tens_fonte / r for r in val_resist]
    return corr_resist, tens_resist

def calc_carga(n_elet):
    CARGA_ELET = 1.6e-19
    return n_elet * CARGA_ELET

def calc_cap_carga(val_carga, tens_fonte):
    return val_carga / tens_fonte

def calc_tens_serie(val_carga, val_capac):
    return [val_carga / c for c in val_capac]

def obter_valores(desc_elem, qtd_elem):
    valores = []
    for i in range(qtd_elem):
        valor = float(input(f"{desc_elem} {i + 1}: "))
        valores.append(valor)
    return valores

def main():
    while True:
        print("\n=== Menu Principal ===")
        tipo_elem = input("Deseja trabalhar com capacitores ou resistores? ").strip().lower()

        if tipo_elem in ["capacitores", "resistores"]:
            tipo_cfg = input("Configuração (serie ou paralelo): ").strip().lower()
            qtd_elem = int(input(f"Quantidade de {tipo_elem}: "))
            tens_fonte = float(input("Tensão da fonte (V): "))

            if tipo_elem == "capacitores":
                val_capac = obter_valores("Capacitância do capacitor (F)", qtd_elem)
                cap_eq = calc_capac(val_capac, tipo_cfg)
                print(f"\nCapacitância Equivalente ({tipo_cfg}): {cap_eq:.2e} F")

                if tipo_cfg == "serie":
                    carga_total = cap_eq * tens_fonte
                    tens_capac = calc_tens_serie(carga_total, val_capac)
                    print("\nTensão em cada capacitor:")
                    for i, tens in enumerate(tens_capac):
                        print(f"Capacitor {i + 1}: {tens:.2f} V")

            elif tipo_elem == "resistores":
                val_resist = obter_valores("Resistência do resistor (Ω)", qtd_elem)
                res_eq = calc_resist(val_resist, tipo_cfg)
                corr_resist, tens_resist = calc_corr_tens(val_resist, tens_fonte, tipo_cfg)

                print(f"\nResistência Equivalente ({tipo_cfg}): {res_eq:.2f} Ω")
                print(f"Corrente Total: {sum(corr_resist):.2f} A" if tipo_cfg == "paralelo" else f"Corrente Total: {corr_resist[0]:.2f} A")
                print("\nDetalhes por Resistor:")
                for i in range(qtd_elem):
                    print(f"Resistor {i + 1}: Corrente = {corr_resist[i]:.2f} A, Tensão = {tens_resist[i]:.2f} V")
        else:
            print("Opção inválida! Tente novamente.")
            continue

        if input("\nDeseja realizar outro cálculo? (s/n): ").strip().lower() != 's':
            print("Encerrando... Até mais!")
            break

if __name__ == "__main__":
    main()
