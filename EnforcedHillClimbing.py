import time
from collections import deque
from solver import PuzzleSolver
from collections import deque

def calculateHeuristic(stateBoard, goalBoard, heuristicType):
    if heuristicType == 1:
        misplaced = 0
        for i in range(len(stateBoard)):

            for j in range(len(stateBoard[0])):

                if stateBoard[i][j] != 0 and stateBoard[i][j] != goalBoard[i][j]:

                    misplaced += 1

        return misplaced
    
    elif heuristicType == 2:

        dist = 0
        positions = {}

        for i in range(len(goalBoard)):

            for j in range(len(goalBoard[0])):

                tile = goalBoard[i][j]
                positions[tile] = (i, j)
        
        for i in range(len(stateBoard)):

            for j in range(len(stateBoard[0])):

                tile = stateBoard[i][j]

                if tile != 0:

                    goalI, goalJ = positions[tile]
                    dist += abs(i - goalI) + abs(j - goalJ)
        return dist
    
    return 0

def enforcedHillClimbing(initialBoard, goalBoard, heuristicType):
    startTime = time.time()
    

    solver = PuzzleSolver(initialBoard, goalBoard)
    initialState = solver.initialState
    goalState = solver.goalState
    

    if solver.isGoal(initialState):
        endTime = time.time()
        print("\nEnforced Hill Climbing Steps:")
        initialState.printBoard()
        return {
            'path': [initialState],
            'pathLength': 0,
            'statesGenerated': 0,
            'executionTime': (endTime - startTime) * 1000,
            'valid': True
        }
    
    statesGenerated = 0
    currentState = initialState
    currentH = calculateHeuristic(currentState.board, goalState.board, heuristicType)
    
    solutionPath = [currentState]
    
    while True:
        neighbors = []
        for move in currentState.getPossibleMoves():
            neighborState = currentState.makeMove(move)
            statesGenerated += 1
            hVal = calculateHeuristic(neighborState.board, goalState.board, heuristicType)
            neighbors.append((neighborState, hVal))
        
        neighbors.sort(key=lambda x: x[1])
        
        bestNeighbor, bestH = None, float('inf')
        for nState, hVal in neighbors:
            if hVal < bestH:
                bestNeighbor, bestH = nState, hVal
        
        if bestNeighbor and bestH < currentH:
            currentState = bestNeighbor
            currentH = bestH
            solutionPath.append(currentState)

            #print(f"\n[Local Move] Found better state (h={bestH}):")
            #currentState.print_board()
            
            if solver.isGoal(currentState):
                endTime = time.time()
                print("\nEnforced Hill Climbing Steps (full path):")
                for i, st in enumerate(solutionPath):
                    print(f"Step {i}:")
                    st.printBoard()
                
                return {
                    'path': solutionPath,
                    'pathLength': len(solutionPath) - 1,
                    'statesGenerated': statesGenerated,
                    'executionTime': (endTime - startTime) * 1000,
                    'valid': solver.validateSolution(solutionPath)
                }
        else:
            probeResult = probeForBetterState(currentState, goalState, currentH, heuristicType)
            
            if probeResult is None:
                endTime = time.time()

                return None
            
            else:
                pathViaBFS = probeResult['path']
                statesGenerated += probeResult['statesGenerated']
                
                for stateInBFS in pathViaBFS[1:]:
                    currentState = stateInBFS
                    currentH = calculateHeuristic(currentState.board, goalState.board, heuristicType)
                    solutionPath.append(currentState)
                    

                    #print(f"\n[Probe Move] BFS found better state (h={currentH}):")
                    #currentState.printBoard()
                    
                    # If we reached the goal in that BFS path
                    if solver.isGoal(currentState):
                        endTime = time.time()
                        print("\nEnforced Hill Climbing Steps (full path):")
                        for i, st in enumerate(solutionPath):
                            print(f"Step {i}:")
                            st.printBoard()
                        
                        return {
                            'path': solutionPath,
                            'pathLength': len(solutionPath) - 1,
                            'statesGenerated': statesGenerated,
                            'executionTime': (endTime - startTime) * 1000,
                            'valid': solver.validateSolution(solutionPath)
                        }


def probeForBetterState(startState, goalState, currentH, heuristicType): 
    queue = deque([(startState, [startState])])
    visited = set([str(startState.board)])
    statesGenerated = 0

    while queue:
        currentNode, path = queue.popleft()
        
        for move in currentNode.getPossibleMoves():
            newState = currentNode.makeMove(move)
            boardStr = str(newState.board)
            if boardStr not in visited:
                visited.add(boardStr)
                statesGenerated += 1
                
                newPath = path + [newState]
                
                hVal = calculateHeuristic(newState.board, goalState.board, heuristicType)
                
                if hVal < currentH:
                    return {'path': newPath, 'statesGenerated': statesGenerated}
                
                queue.append((newState, newPath))
    
    return None