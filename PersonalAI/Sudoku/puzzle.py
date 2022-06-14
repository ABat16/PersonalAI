class Puzzle:

    #initializer
    def __init__(self, board):
        '''
        Maybe on instantiation the puzzle importer passes in a 
        CSV object for the puzzle object to parse and add to the 
        board variable?
        '''
        self.board = board
        self.variables = self.buildVariables()      # array containing cords to each cell
        self.peers = self.buildPeers()              # array containing cords to each cells set of conflicting neighbors
        self.domains = self.buildDomains()          # array containing the possible values for each cell


    # replaces values in row,col of board with val
    def update_board(self, row, col, val):
        self.board.iloc[row, col] = val

    # prints board
    def printBoard(self):
        print(self.board.to_string())

    #adds given value to given cell
    def update_board(self, row, col, val):
        self.board.iloc[row, col] = val

    #prints puzzle
    def printBoard(self):
        print(self.board.to_string())

    #calculates the number of conflicts throughout the board
    def calcConflicts(self):
        conflicts = 0
        # itterate through puzzle
        for row in range(9):
            for col in range(9):
                # get val at row, col
                var = self.board.iloc[row,col]
                # check if val is assigned
                if var != '?':
                    # itterate through conflicting peers of current cell to see if there are any conflicts
                    for p in self.peers[(row * 9) + col]:
                        if var == self.board.iloc[p[0], p[1]]:
                            # itterate if a conflict is found
                            conflicts += 1
        return conflicts

    # builds a array containing all cords to each cell in the puzzle (0,0) -> (8,8)
    def buildVariables(self):
        variables = []
        for row in range(9):
            for col in range(9):
                variables.append([row,col])
        return variables


    # builds an 81 len array with each index containing the 20 conflicting cells to each individual cell
    def buildPeers(self):
        peers = []
        for i in range(81):
            peers.append(self.neighbors(self.variables[i][0], self.variables[i][1]))
        return peers

    # builds an 81 len array containing the domains of each cell
    def buildDomains(self):
        domains = []
        # begin with full domains for each cell
        for i in range(81):
            domains.append(['1','2','3','4','5','6','7','8','9'])

        # itterate through puzzle
        for row in range(9):
            for col in range(9):
                val = self.board.iloc[row,col]
                # if a val exists at row, col
                if val != '?':
                    # replace locations domain with val existing in cell
                    domains[row*9 + col] = [val]

                    # itterate through all conflicting cells of current cell and remove val from their domains
                    for p in self.peers[row * 9 + col]:
                        if val in domains[p[0] * 9 + p[1]]:
                            domains[p[0] * 9 + p[1]].remove(val)
        return domains
    
    # returns the 20 conflicting neighbors to a given cell
    def neighbors(self, row, col):
        nbors = []
        # adds row neighbors
        for i in range(9):
            if i != row:
                nbors.append([i, col])
        # adds col neighbors
        for j in range(9):
            if j != col:
                nbors.append([row, j])   
        # restrics board to section of applicable rows
        if row < 3:
            restrictedBoard = self.board[0:3]
        elif row > 5:
            restrictedBoard = self.board[6:9]
        else:
            restrictedBoard = self.board[3:6]
        # restrics the board to section of applicable columns
        if col < 3:
            region = restrictedBoard[[0,1,2]]  
        elif col > 5:
            region = restrictedBoard[[6,7,8]]
        else:
            region = restrictedBoard[[3,4,5]]
        # itterates through region leaving out already counted neighbors
        for val in region.columns:
            for ind in region.index:
                if val != col and ind != row:
                    nbors.append([ind, val])
        return nbors
