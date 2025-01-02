from PuzzleState import PuzzleState

class PuzzleSolver:
    def __init__(self, initialState, goalState):
        self.initialState = PuzzleState(initialState)
        self.goalState = PuzzleState(goalState)
        
    def isGoal(self, state):
        return state.board == self.goalState.board
        
    def getPath(self, cameFrom, current):
        path = []

        while current in cameFrom:
            path.append(current)
            current = cameFrom[current]

        path.append(self.initialState)
        
        return path[::-1]
        
    def validateSolution(self, path):
        if not path:
            return False
        
        current = PuzzleState(self.initialState.board)

        for nextState in path[1:]:
            moves = current.getPossibleMoves()
            validMove = False

            for move in moves:
                if current.makeMove(move).board == nextState.board:
                    validMove = True
                    current = nextState
                    break

            if not validMove:
                return False
            
        return current.board == self.goalState.board