class Player:
    def __init__(self, cards, gameType):
        self.cards = cards
        self.potentialChain = []
        if gameType == 0:
            self.people = [-1,-1,-1,-1,-1,-1]
            self.weapons = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
            self.places = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        else:
            self.people = [-1,-1,-1,-1,-1,-1]
            self.weapons = [-1,-1,-1,-1,-1,-1]
            self.places = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        if len(self.cards) != 0:
            for i in range(len(self.cards[0])):
                self.people[int(cards[0][i])] = 1

            for i in range(len(self.cards[1])):
                self.weapons[int(cards[1][i])] = 1

            for i in range(len(self.cards[2])):
                self.places[int(cards[2][i])] = 1
                
            for i in range(len(self.people)):
                if self.people[i] == -1:
                    self.people[i] = 0
            for i in range(len(self.weapons)):
                if self.weapons[i] == -1:
                    self.weapons[i] = 0
            for i in range(len(self.places)):
                if self.places[i] == -1:
                    self.places[i] = 0
                    
                    

    def display(self):
        print(self.people)
        print(self.weapons)
        print(self.places)
        
    def doesntHave(self, cards):
        self.people[int(cards[0])] = 0
        self.weapons[int(cards[1])] = 0
        self.places[int(cards[2])] = 0
        
    def updateInfo(self, cardType, num):
        if cardType == 0:
            self.people[num] = 1
        elif cardType == 1:
            self.weapons[num] = 1
        elif cardType == 2:
            self.places[num] = 1
            
    def HasOneOfThem(self, guess):
        self.potentialChain.append(guess)
        
    def eliminateDomain(self, cardType, num):
        if cardType == 0:
            self.people[num] = 0
        elif cardType == 1:
            self.weapons[num] = 0
        elif cardType == 2:
            self.places[num] = 0
            

