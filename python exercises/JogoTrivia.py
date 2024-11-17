import random

def apresentar_pergunta(pergunta, opcoes, resposta_correta):
    print(pergunta)
    for opcao in opcoes:
        print(opcao)
    
    resposta = input("Digite a letra da sua resposta: ").upper()
    return resposta == resposta_correta

def rodar_jogo(perguntas):
    score = 0

    for pergunta in perguntas:
        pergunta_texto, opcoes, resposta_correta = pergunta
        acertou = apresentar_pergunta(pergunta_texto, opcoes, resposta_correta)
        if acertou:
            print("Resposta correta!")
            score += 1
        else:
            print("Resposta errada!")
        print()

    print(f"Seu score final: {score} de {len(perguntas)}")

def main():
    perguntas = [
        ("Qual é a capital da França?", 
         ["A) Marselha", "B) Lyon", "C) Paris", "D) Nice"], 
         "C"),
        ("Quem pintou a Mona Lisa?", 
         ["A) Vincent Van Gogh", "B) Pablo Picasso", "C) Leonardo Da Vinci", "D) Michelangelo"],
         "C"),
        ("Qual é o maior planeta do Sistema Solar?", 
         ["A) Terra", "B) Jupiter", "C) Saturno", "D) Marte"],
         "B"),
        ("Qual é o elemento quimico com o simbolo 'O'?", 
         ["A) Ouro", "B) Oxigênio", "C) Osmio", "D) Ferro"],
         "B"),
        ("Qual idioma é  tradicionalmente falado no Brasil?", 
         ["A) Inglês", "B) Espanhol", "C) Francês", "D) Portugues"],
         "D")
    ]

    random.shuffle(perguntas)
    rodar_jogo(perguntas)

if __name__ == "__main__":
    main()
