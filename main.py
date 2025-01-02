from BreathFirstSearch import breathFirstSearch
from EnforcedHillClimbing import enforcedHillClimbing

initialBoard = [
    [2, 4, 3],
    [1, 5, 6],
    [7, 0, 8]
]

goalBoard = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def mainMenu():
    print("\nSliding Puzzle Solver")
    print("1. Breadth First Search")
    print("2. Greedy Best First Search")
    print("3. A* Search")
    print("4. Enforced Hill Climbing")
    print("5. Exit")
    userChoice = input("Enter your choice: ")

    try:
        userChoice = int(userChoice)
        if userChoice == 5:
            print("Goodbye!")
            exit()

        elif userChoice in range(1, 5):
            searchResult = None
            
            if userChoice in [2, 3, 4]:
                print("Select Heuristic")
                print("1. Misplaced Tiles")
                print("2. Manhattan Distance")
                heuristicChoice = int(input("Enter your choice: "))
                
                if not heuristicChoice in range(1, 3):
                    print("Invalid heuristic choice")
                    return
            else:
                heuristicChoice = None
            
            if userChoice == 1:
                searchResult = breathFirstSearch(initialBoard, goalBoard)

            elif userChoice == 4:
                searchResult = enforcedHillClimbing(initialBoard, goalBoard, heuristicChoice)
            
            if searchResult:
                print(f"\nSolution found!")
                print(f"Path length: {searchResult['pathLength']}")
                print(f"States generated: {searchResult['statesGenerated']}")
                print(f"Execution time: {searchResult['executionTime']:.2f} ms")
                print(f"Solution is {'valid' if searchResult['valid'] else 'invalid'}")

            else:
                print("\nNo solution found")
        else:
            print("Invalid choice")
            
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    while True:
        mainMenu()