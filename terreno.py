def calcularArea(comprimento, largura):
    area = comprimento * largura
    return area

comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite a largura do terreno em metros: "))

area_terreno = calcularArea(comprimento, largura)
print("A área do terreno é: {:.2f} metros quadrados".format(area_terreno))
