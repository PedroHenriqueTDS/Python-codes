while True:
    while True:
        n1 = int(input("Primeiro numero: "))
        n2 = int(input("Segundo numero: "))

        print("1- Adição")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5- Sair")
        op = int(input("Digite o índice da opção: "))
        
        if op == 1:
            n3 = n1 + n2
            print(n3)
        
        elif op == 2:
            n3 = n1 - n2
            print(n3)

        elif op == 3:
            n3 = n1 * n2
            print(n3)

        elif op == 4:
            if n2 == 0:
                print("Erro: Divisão por zero.")
            else:
                n3 = n1 / n2
                print(n3)
        
        elif op == 5:
            break  
        
        else:
            print("Opção inválida!")
    
    sair = input("Deseja sair do programa? (S/N): ").upper()
    if sair == "S":
        break
