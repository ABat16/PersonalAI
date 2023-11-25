import numpy as np
class gameBoard:
    rotation1 = []
    rotation2 = []
    rotation3 = []
    rotation4 = []
    r1 = True
    r2 = True
    r3 = True
    r4 = True
    def __init__(self, board):
        self.rotation1 = np.array(board)
        self.genRotations()
        self.r1 = True
        self.r2 = True
        self.r3 = True
        self.r4 = True

    def genRotations(self):
        #print(self.rotation1)
        #print('\n')
        self.rotation2 = np.transpose(self.rotation1)
        self.rotation2 = np.flip(self.rotation2, axis = 1)
        #print(self.rotation2)
        #print('\n')
        self.rotation3 = np.transpose(self.rotation2)
        self.rotation3 = np.flip(self.rotation3, axis = 1)
        #print(self.rotation3)
        #print('\n')
        self.rotation4 = np.transpose(self.rotation3)
        self.rotation4 = np.flip(self.rotation4, axis = 1)
        #print(self.rotation4)
        #print('\n')

    def validateGuessBoard(self, gBoard):
        for i in range(5):
            for j in range(5):
                if gBoard[i,j] != -1:
                    if self.rotation1[i,j] != gBoard[i,j]:
                        self.r1 = False
                    if self.rotation2[i,j] != gBoard[i,j]:
                        self.r2 = False
                    if self.rotation3[i,j] != gBoard[i,j]:
                        self.r3 = False
                    if self.rotation4[i,j] != gBoard[i,j]:
                        self.r4 = False
    def printPossibleRotations(self):
        if self.r1:
            print(self.rotation1)
        elif self.r2:
            print(self.rotation2)
        elif self.r3:
            print(self.rotation3)
        elif self.r4:
            print(self.rotation4)
        
