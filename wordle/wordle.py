import numpy as np
import pyautogui
import time
import random
class wordle:
    def __init__(self):
        self.keyboard = {'Q':(737,866),
                    'W':(788,866),
                    'E':(837,866),
                    'R':(885,866),
                    'T':(935,866),
                    'Y':(983,866),
                    'U':(1035,866),
                    'I':(1085,866),
                    'O':(1135,866),
                    'P':(1185,866),
                    'A':(761,933),
                    'S':(811,933),
                    'D':(861,933),
                    'F':(911,933),
                    'G':(961,933),
                    'H':(1011,933),
                    'J':(1061,933),
                    'K':(1111,933),
                    'L':(1161,933),
                    'Z':(811,999),
                    'X':(861,999),
                    'C':(911,999),
                    'V':(961,999),
                    'B':(1011,999),
                    'N':(1061,999),
                    'M':(1111,999),
                    'ENTER': (751,1000),
                    'BACKSPACE': (1170,1000)}
        self.gameboard = [[(841,328),(910,328),(974,328),(1042,328),(1110,328)],
                     [(841,394),(910,394),(974,394),(1042,394),(1110,394)],
                     [(841,460),(910,460),(974,460),(1042,460),(1110,460)],
                     [(841,531),(910,531),(974,531),(1042,531),(1110,531)],
                     [(841,594),(910,594),(974,594),(1042,594),(1110,594)],
                     [(841,664),(910,664),(974,664),(1042,664),(1110,664)]]

        self.letterPool = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                      'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        self.TheBadBoys = []
        self.TheGoodBoys = []
        self.TheCuties = []    # Reset The Cuties After Each turn

        self.Green = (83, 141, 78)
        self.Yellow = (181, 159, 59)
        self.Black = (58,58,60)
        self.White = (215, 218, 220)

        self.words = []
        self.MakeDaWords()
        
        self.gameState = 0
        self.prevWord = 'PENIS'

    def InitPenis(self):
        time.sleep(1)
        self.doWord('PENIS')
##        pyautogui.click(self.keyboard['P'])
##        pyautogui.click(self.keyboard['E'])
##        pyautogui.click(self.keyboard['N'])
##        pyautogui.click(self.keyboard['I'])
##        pyautogui.click(self.keyboard['S'])
##        pyautogui.click(self.keyboard['ENTER'])
##        self.prevWord = 'PENIS'
##        self.TakeABreak()

    def MakeDaWords(self):
        file = open('wordbase.txt', 'r')
        for word in file:
            word = word.strip()
            self.words.append(word)
        file.close()
            
    def TheCulling(self):

        theCulled = []
        for word in self.words:
            #print(word)
            cul = False
            for cutie in self.TheCuties:
                #print(cutie)
                if cutie not in word:
                    #print('yaa')
                    cul = True
            for badboy in self.TheBadBoys:
                #print(badboy)
                if badboy in word:
                    #print('yee')
                    cul = True
            for goodboy in self.TheGoodBoys:
               # print(goodboy)
                if word[goodboy[1]] != goodboy[0]:
                    #print('yoo')
                    cul = True
            if cul:
                theCulled.append(word)
        for cullin in theCulled:
            self.words.remove(cullin)

                    

    def MostWanted(self, badboy):
        self.TheBadBoys.append(badboy)

    def MegaCute(self, goodboy):
        self.TheGoodBoys.append(goodboy)

    def MegaCute(self, cutie):
        self.TheCuties.append(cutie)

    def GetRidOfEm(self):
        self.TheCuties = []
        self.TheGoodBoys = []

    def doWord(self,word):
        print(word)
        for i in range(5):
            pyautogui.click(self.keyboard[word[i]])
            time.sleep(.1)
        pyautogui.click(self.keyboard['ENTER'])
        time.sleep(.05)
        im = pyautogui.screenshot()
        px = im.getpixel((956,250))
        
        if px == self.White:
            self.YouStupid(word)
            print(word + " Eliminated From File")
        else:
            self.prevWord = word
            self.TakeABreak()

    def TakeTurn(self):
        im = pyautogui.screenshot()
        for i in range(5):
            px = im.getpixel(self.gameboard[self.gameState][i])
            if px == self.Green:
                self.TheGoodBoys.append((self.prevWord[i], i))
            if px == self.Yellow:
                self.TheCuties.append(self.prevWord[i])
            if px == self.Black:
                nope = True
                for val in self.TheGoodBoys:
                    if self.prevWord[i] in val:
                        nope = False
                if self.prevWord[i] not in self.TheCuties and nope:
                    self.TheBadBoys.append(self.prevWord[i])

        # Letters are being added to badboys when they are in goodboys
                
            
                
        self.TheCulling()
        print(self.words)
        print(self.TheGoodBoys)
        print(self.TheBadBoys)
        print(self.TheCuties)

        self.doWord(self.words[0])
        self.GetRidOfEm()
        self.gameState+=1

    def YouStupid(self, word):
        with open('wordbase.txt', 'r') as f:
            lines = f.readlines()
        with open('wordbase.txt','w') as f:
            for line in lines:
                if line.strip('\n') != word:
                    f.write(line)
    
    def TakeABreak(self):
        time.sleep(2)
                
        




wordle = wordle()
wordle.InitPenis()
for i in range(5):
    wordle.TakeTurn()

##while True:
##    print(pyautogui.position())
##im = pyautogui.screenshot()
##px = im.getpixel((956,250))
##print(px)





