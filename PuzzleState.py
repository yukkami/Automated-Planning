class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.size = 3
        self.emptyCell = self.findEmpty()
    
    def findEmpty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
                
        return None

    def getPossibleMoves(self):
        possibleMoves = []
        row, col = self.emptyCell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            newRow, newCol = row + dx, col + dy

            if 0 <= newRow < self.size and 0 <= newCol < self.size:
                possibleMoves.append((newRow, newCol))

        return possibleMoves

    def makeMove(self, move):
        newBoard = [row[:] for row in self.board]
        emptyRow, emptyCol = self.emptyCell
        newRow, newCol = move
        
        newBoard[emptyRow][emptyCol] = newBoard[newRow][newCol]
        newBoard[newRow][newCol] = 0
        
        return PuzzleState(newBoard)
        
    def printBoard(self):
        for row in self.board:
            print("+----+----+----+")
            print("|", end=" ")
            
            for cell in row:
                if cell == 0:
                    print("  ", end=" | ")
                else:
                    print(f"{cell:2}", end=" | ")
            print()
        print("+----+----+----+")