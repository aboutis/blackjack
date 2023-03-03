import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer = []
player = []

def deal_card(lista, number):
    num = random.choices(deck, k=number)
    for i in num:
        lista.append(i)

def blackjack(lista):
    soma = sum(lista)
    if soma > 21:
        for i in lista:
            if i == 11:
                soma -= 10
                if soma == 21:
                    return 0
                else:
                    return 1
    if soma == 21:
        return 0
    if soma < 16:
        return 2

deal_card(computer, 2)
deal_card(player, 2)
print(f"A primeira carta do computador é {computer[0]}.")
print(f"Suas cartas são: {player}")

def checagem():
    retorno_comp = blackjack(computer)
    retorno_ply = blackjack(player)
    fim = True
    while fim:
        if retorno_comp == 0:
            print("Fim de jogo. Computador ganhou.!")
            print(f"As cartas do computador eram: {computer}")
            fim = False
        else:
            if retorno_ply == 0:
                print("Você ganhou. Parabéns!")
                fim = False
            else:
                if retorno_comp == 1 and retorno_ply != 1:
                    print("A soma das cartas do computador é maior que 21. Você ganhou!")
                    fim = False
                elif retorno_ply == 1 and retorno_comp != 1:
                    print("A soma das suas cartas é maior que 21. Você perdeu!")
                elif retorno_comp == 2:
                    continuar = input("Você deseja outra carta? (sim/nao): ")
                    if continuar == "sim":
                        deal_card(player, 1)
                        retorno_ply = blackjack(player)
                        print(f"Suas cartas são {player}")
                        checagem()
                    if continuar == "nao":
                        deal_card(computer, 1)
                        retorno_comp = blackjack(computer)
                        checagem()

checagem()

