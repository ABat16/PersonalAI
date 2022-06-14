import queue
class Backtrack_AC():
    
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.queue = queue.Queue()

    def solve(self):
        self.decisionCount = 0
        self.recursiveAC(0,0)
        return self.puzzle

    def recursiveAC(self, row, col):
        self.decisionCount += 1

        # iterates through rows and columns
        if col == 9:
            row += 1
            col = 0

        # checks if puzzle is complete
        if self.puzzleIsComplete():

            # if AC fails then there will be conflicts
            conflicts = self.puzzle.calcConflicts()
            print("Num Conflicts: " + str(conflicts))
            if conflicts == 0:
                print("AC Worked")
            else:
                print("AC Failed")
            
            self.puzzle.printBoard()
            print()
            return self.puzzle

        # if current cell is ? skip
        if self.puzzle.board.iloc[row,col] != '?':
            return self.recursiveAC(row, col + 1)

        # iterates through possible vals in current cells domain
        for i in self.puzzle.domains[row *9 + col]:

            # updates the board with current val
            self.puzzle.update_board(row, col, i)

            # eliminates val from the domains of conflicting cells
            self.puzzle.domains = self.puzzle.buildDomains()

            # attempts to make puzzle arc consistent
            if self.checkAC():
                # if puzzle is arc consistent then do the same with the next cell
                if self.recursiveAC(row, col + 1):
                    return True
            # if puzzle cannot be made arc consistent then iterate through domain and replace selected val
            self.puzzle.update_board(row,col,'?')
            self.puzzle.domains = self.puzzle.buildDomains()
        # if no vals in domain work then backtrack
        return False
                        
        
    def checkAC(self):
        # build queue of all arcs in puzzle
        self.buildQueue()

        # process through queue
        while not self.queue.empty():
            # take the first arc from queue
            (Xi, Xj) = self.queue.get()

            # check for inconsistent values in the domains of the first arc
            if self.removeInconsistentValues(Xi, Xj):

                # if the len of a domain is 0 then arc consistency failed and return false
                if len(self.puzzle.domains[Xi[0] * 9 + Xi[1]]) == 0:
                    return False
                # once the inconsistent values are removed switch arcs and place back into queue
                for Xk in self.puzzle.peers[Xi[0] * 9 + Xi[1]]:
                
                    self.queue.put([Xk, Xi])
        # If puzzle is arc consistent return true
        return True

                    
    def removeInconsistentValues(self, Xi, Xj):
        removed = False
        # Pick a value from the domain of one cell
        for x in self.puzzle.domains[Xi[0] * 9 + Xi[1]]:
            # check value is consistent with all domains in other cell
            if not self.isConsistent(x, Xi, Xj):
                # if there is a conflict remove x from domain
                self.puzzle.domains[Xi[0] * 9 + Xi[1]].remove(x)
                removed = True
        return removed

    def isConsistent(self, x, Xi, Xj):
        # compare all values in domain of second cell with val x in first cell looking for conflictions
        for y in self.puzzle.domains[Xj[0] * 9 + Xj[1]]:
            if y!=x:
                return True
        return False


    def buildQueue(self):
        # builds a queue with all conflictions in puzzle
        for i in range(81):
            for p in self.puzzle.peers[i]:
                self.queue.put([self.puzzle.variables[i], p])

    def puzzleIsComplete(self):
        for i in range(9):
            for j in range(9):
                val = self.puzzle.board.iloc[i,j]
                if val == '?':
                    return False

        return True
