from collections import deque
import time
from solver import PuzzleSolver

def breathFirstSearch(initialBoard, goalBoard):
    startTime = time.time()
    solver = PuzzleSolver(initialBoard, goalBoard)
    initialState = solver.initialState
    stateQueue = deque([(initialState, [])])
    visitedStates = set()
    statesGenerated = 0
    
    print("\nInitial State:")
    initialState.printBoard()
    
    visitedStates.add(str(initialState.board))
    
    while stateQueue:
        currentState, statePath = stateQueue.popleft()
        
        if solver.isGoal(currentState):
            statePath = statePath + [currentState]
            endTime = time.time()
            executionTime = (endTime - startTime) * 1000
            
            print("\nSolution Path:")
            for i, state in enumerate(statePath):
                print(f"\nStep {i}:")
                state.printBoard()
            
            return {
                'path': statePath,
                'pathLength': len(statePath) - 1,
                'statesGenerated': statesGenerated,
                'executionTime': executionTime,
                'valid': solver.validateSolution(statePath)
            }
            
        for move in currentState.getPossibleMoves():
            newState = currentState.makeMove(move)
            boardStr = str(newState.board)
            
            if boardStr not in visitedStates:
                statesGenerated += 1
                visitedStates.add(boardStr)
                stateQueue.append((newState, statePath + [currentState]))
    
    return None