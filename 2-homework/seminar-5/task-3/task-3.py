# Создайте программу для игры в ""Крестики-нолики"".

board = [i+1 for i in range(9)]
def Game(board):
    counter = 0
    win = False
    while not win:
        BoardDraw(board)
        if counter % 2 == 0:
            Placement("X")
        else:
            Placement("O")
        counter += 1
        if counter > 4:
            checkWin = CheckWin(board)
            if checkWin:
                print(checkWin, "Won!")
                win = True
                break
        if counter == 9:
            print("Draw!")
            break
    BoardDraw(board)

Game(board)


def BoardDraw(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")


def Placement(playerID):
    moveDone = False
    while not moveDone:
        playerInput = int(input(playerID + ", where to input? "))
        if playerInput >= 1 and playerInput <= 9:
            if (str(board[playerInput-1]) not in "XO"):
                board[playerInput-1] = playerID
                moveDone = True
            else:
                print("This cell is alredy filled")
        else:
            print("Input is mistaken")

def CheckWin(board):
    victoryCoords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in victoryCoords:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False



