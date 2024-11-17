import itertools
import os
import time
import random


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimirtab(tab):
    limpar()
    print("  0 | 1 | 2 ")
    print(" ---------")
    print("  3 | 4 | 5 ")
    print(" ---------")
    print("  6 | 7 | 8 ")
    print("\n")
    print("Tabuleiro Atual:")
    print(" -------------")
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print(" ---------")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print(" ---------")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")

def verificaV(tab, player):
    combinaçõesVitoria = [
        [tab[0], tab[1], tab[2]],
        [tab[3], tab[4], tab[5]],
        [tab[6], tab[7], tab[8]],
        [tab[0], tab[3], tab[6]],
        [tab[1], tab[4], tab[7]],
        [tab[2], tab[5], tab[8]],
        [tab[0], tab[4], tab[8]],
        [tab[2], tab[4], tab[6]]
    ]
    return [player, player, player] in combinaçõesVitoria

def play():
    jogadores = ['X', 'O']
    tab = [' ' for _ in range(9)]
    turno = random.choice([0, 1])
    pA = True

    while pA:
        imprimirtab(tab)
        jogadoratual = jogadores[turno]
        print(f'Vez do player {jogadoratual}')

        posicao = None
        while posicao not in range(9) or tab[posicao] != ' ':
            try:
                posicao = int(input('Escolha uma posição (0-8): '))
            except ValueError:
                pass

        tab[posicao] = jogadoratual

        if verificaV(tab, jogadoratual):
            imprimirtab(tab)
            print(f"Parabéns! O player {jogadoratual} venceu!")
            pA = False
        elif ' ' not in tab:
            imprimirtab(tab)
            print("Empate!")
            pA = False
        else:
            turno = (turno + 1) % 2

        time.sleep(1)

if __name__ == "__main__":
    play()
