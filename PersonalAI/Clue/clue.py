from Player import Player
class Clue:
    def __init__(self, numPlayers, starter, gameType = 0):
        self.gameType = gameType
        if self.gameType == 0:
            self.people = {
                0: "Mustard",
                1: "Plum",
                2: "Green",
                3: "Peacock",
                4: "Scarlet",
                5: "White"
                }
            self.weapons = {
                0: "Knife",
                1: "Candlestick",
                2: "Pistol",
                3: "Poison",
                4: "Trophy",
                5: "Rope",
                6: "Bat",
                7: "Ax",
                8: "Dumbbell"
                }
            self.places = {
                0: "Hall",
                1: "Dining Room",
                2: "Kitchen",
                3: "Patio",
                4: "Observatory",
                5: "Theater",
                6: "Living Room",
                7: "Spa",
                8: "Guest House"
                }
        else:
            self.people = {
                0: "Dr. Orchid",
                1: "Mr. Green",
                2: "Mrs. Peacock",
                3: "Miss Scarlett",
                4: "Mustard",
                5: "Mme. Rose"
                }
            self.weapons = {
                0: "Candlestick",
                1: "Dagger",
                2: "Lead Pipe",
                3: "Revolver",
                4: "Rope",
                5: "Wrench"
                }
            self.places = {
                0: "Ballroom",
                1: "Billiard Room",
                2: "Conservatory",
                3: "Dining Room",
                4: "Hall",
                5: "Kitchen",
                6: "Library",
                7: "Lounge",
                8: "Study"
                }
        self.playerList = []
        self.numPlayers = numPlayers
        self.starter = starter
        self.locationOnTable = self.numPlayers - self.starter
        self.generateTable()
        self.run = True
        self.play()
        
        

    def play(self):
        curPlayer = self.starter
        while(self.run):
            print("Player " + str(curPlayer) + "'s Turn:")
            if curPlayer == 0:
                YN = input("Do You Make A Guess(y/n): ")         
            else:
                YN = input("Did They Make A Guess(y/n): ")
            if YN == 'y':
                self.printPeople()
                self.printWeapons()
                self.printPlaces()
                guess = input("What Was The Guess: ")
                guess = guess.split(',')
                for i in range(len(guess)):
                    guess[i] = int(guess[i])
                shown = True
                counter = 1
                while shown == True:
                    if (curPlayer + counter)%self.numPlayers != 0:
                        question = input("Can Player " + str((curPlayer + counter)%self.numPlayers) + " Disprove?(y/n)")
                        if question == 'y':
                            shown = False
                            if curPlayer == 0:
                                print("Card Type: \n0 - People\n1 - Weapon\n2 - Place")
                                cardType = int(input("What Type Of Card Was Shown To You?"))
                                if cardType == 0:
                                    card = guess[0]
                                elif cardType == 1:
                                    card = guess[1]
                                elif cardType == 2:
                                    card = guess[2]
                                self.playerList[0].updateInfo(cardType, card)
                                self.playerList[0].display()
                            else:
                                self.playerList[(curPlayer + counter)%self.numPlayers].HasOneOfThem(guess)
                                
                        else:
                            self.playerList[(curPlayer + counter)%self.numPlayers].doesntHave(guess)
##                            for player in self.playerList:
##                                    player.display()
                    else:
                        Your = input("Your Turn, Can You Disprove(y/n)")
                        if Your == 'y':
                            shown = False
                        
                    counter+=1
                    if counter == self.numPlayers:
                        shown = False
                self.doAnalysis()
                self.checkForTarget()
            curPlayer +=1
            curPlayer = curPlayer%self.numPlayers

    def checkForTarget(self):
        personC = 0
        weaponC = 0
        placeC = 0

        culprit = -1
        stick = -1
        addy = -1
        
        for i in range(len(self.playerList[0].people)):
            if self.playerList[0].people[i] == 1:
                personC +=1
            if self.playerList[0].people[i] == 0:
                culprit = i
        for i in range(len(self.playerList[0].weapons)):
            if self.playerList[0].weapons[i] == 1:
                weaponC += 1
            if self.playerList[0].weapons[i] == 0:
                stick = i
        for i in range(len(self.playerList[0].places)):
            if self.playerList[0].places[i] == 1:
                placeC +=1
            if self.playerList[0].places[i] == 0:
                addy = i
        if personC == len(self.playerList[0].people) - 1:
            input("Culprit Discovered!")
            print("The Culprit is " + self.people[culprit])
            input()
        if weaponC == len(self.playerList[0].weapons) - 1:
            input("Weapon Discovered!")
            print("The Weapon Used Was The " + self.weapons[stick])
            input()
        if placeC == len(self.playerList[0].places) - 1:
            input("Location Discovered!")
            print("The Location Of The Crime Was The " + self.places[addy])
            input()
        if personC == len(self.playerList[0].people) - 1 and weaponC == len(self.playerList[0].weapons) - 1 and placeC == len(self.playerList[0].places) - 1:
            input("The Scandal Has Been Solved!")
            print("Person: " + self.people[culprit] + "\nWeapon: " + self.weapons[stick] + "\nLocation: " + self.places[addy])
            self.run = False


            
    
    def doAnalysis(self):
        for i in range(1, self.numPlayers):
            targets = []
            for j in range(len(self.playerList[i].potentialChain)):
                target = self.playerList[i].potentialChain.pop()
                if self.playerList[i].people[target[0]] == 0 and self.playerList[i].weapons[target[1]] == 0:
                    self.playerList[0].updateInfo(2,target[2])
                    self.playerList[i].updateInfo(2,target[2])
                elif self.playerList[i].people[target[0]] == 0 and self.playerList[i].places[target[2]] == 0:
                    self.playerList[0].updateInfo(1,target[1])
                    self.playerList[i].updateInfo(1,target[1])
                elif self.playerList[i].places[target[2]] == 0 and self.playerList[i].weapons[target[1]] == 0:
                    self.playerList[0].updateInfo(0,target[0])
                    self.playerList[i].updateInfo(0,target[0])
                else:
                    targets.append(target)
            for val in targets:
                self.playerList[i].potentialChain.append(val)
        for i in range(len(self.playerList[0].people)):
            if self.playerList[0].people[i] == 1:
                for j in range(1,self.numPlayers):
                    self.playerList[j].eliminateDomain(0,i)

        for i in range(len(self.playerList[0].weapons)):          
            if self.playerList[0].weapons[i] == 1:
                for j in range(1,self.numPlayers):
                    self.playerList[j].eliminateDomain(1,i)
                    
        for i in range(len(self.playerList[0].places)):
            if self.playerList[0].places[i] == 1:
                for j in range(1,self.numPlayers):
                    self.playerList[j].eliminateDomain(2,i)
                
        
    
    def generateTable(self):
        peopleCards = []
        weaponCards = []
        placeCards = []
        
        peopleYN = input("Do You Have Any People Cards?(y/n)")
        if peopleYN == 'y':
            self.printPeople()
            peopleCards = input("Which?")
            peopleCards = peopleCards.split(',')
        
        weaponYN = input("Do You Have Any Weapon Cards?(y/n)")
        if weaponYN == 'y':
            self.printWeapons()
            weaponCards = input("Which?")
            weaponCards = weaponCards.split(',')
            
        placeYN = input("Do You Have Any Place Cards?(y/n)")
        if placeYN == 'y':
            self.printPlaces()
            placeCards = input("Which?")
            placeCards = placeCards.split(',')
            
             
        yourCards = [peopleCards,weaponCards,placeCards]
        print(yourCards)
        for i in range(self.numPlayers):
            if i == 0:
                self.playerList.append(Player(yourCards,self.gameType))
            else:
                self.playerList.append(Player([],self.gameType))
            self.playerList[i].display()
            
        
    def printPeople(self):
        for i in range(len(self.people)):
            val = str(i) + ': ' + self.people[i]
            print(val)
        print('\n')
    def printWeapons(self):
        for i in range(len(self.weapons)):
            val = str(i) + ': ' + self.weapons[i]
            print(val)
        print('\n')
    def printPlaces(self):
        for i in range(len(self.places)):
            val = str(i) + ': ' + self.places[i]
            print(val)
        print('\n')
        
            
