# Создайте программу для игры с конфетами человек против человека.

import random

total = 2021
player1 = str(input(" Player 1 input yr name: "))
player2 = str(input(" Player 2 input yr name: "))
playersList = list([player1,player2])
FirstMove = random.randint(0,1)

def Game():
    global total
    while total !=0:
        Move(playersList[FirstMove])
        if total == 0:
            print(f"  {playersList[FirstMove]} won! ")
        Move(playersList[-1 + FirstMove])
        if total == 0:
            print(f"  {playersList[-1 + FirstMove]} won! ")

def Move(player):
    global total
    playerNumber = int(input(f"  {player} your move: "))
    total -= playerNumber
    print(f" {total}")


Game()

# Добавьте игру против бота

total = 2021
player = str(input(" Player 1 input yr name: "))
bot = "Bot"
playersList = list([player,bot])
FirstMove = random.randint(0,1)

def Game():
    global total
    while total !=0:
        Move(playersList[FirstMove])
        if total == 0 or total < 0:
            print(f"  {playersList[FirstMove]} won! ")
        Move(playersList[-1 + FirstMove])
        if total == 0 or total < 0:
            print(f"  {playersList[-1 + FirstMove]} won! ")

def Move(player):
    global total
    if player != "Bot":
        playerNumber = int(input(f"  {player} your move: "))
        total -= playerNumber
        print(f" {total}")
    else:
        topR = 28 
        if total < topR:
            topR = total
        rBot = random.randrange(1,topR+1)
        total -= rBot 
        print(f"  Bot move: {rBot}\n", total)

Game()