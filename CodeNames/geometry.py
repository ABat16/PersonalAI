from gameBoard import gameBoard
import numpy as np

GuessingBoard = np.ones((5,5), dtype = int)
GuessingBoard = GuessingBoard * -1

def playGame():
    token = 0
    while token != '-1':
        token = input("Location and token (-1 to continue): ")
        if token != '-1':
            token = token.split(' ')
            GuessingBoard[int(token[0]), int(token[1])] = int(token[2])
            print(GuessingBoard)
    for i in range(len(boards)):
        boards[i].validateGuessBoard(GuessingBoard)
        boards[i].printPossibleRotations()
        

file = open('boards.txt', 'r').read()

raw = file.split('\n')
curBoard = []
boards = []
for line in raw:
    if line != '':
        appendLine = []
        line = line.split(',')
        for i in range(len(line)):
            if line[i] != '':
                appendLine.append(int(line[i]))
        curBoard.append(appendLine)
    else:
        if len(curBoard) != 0:
            boards.append(gameBoard(curBoard))
        curBoard = []
play = 'y'
while play == 'y':
    playGame()
    play = input("Keep Playing: ")
