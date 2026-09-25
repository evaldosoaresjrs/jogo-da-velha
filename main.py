from utils import *

# Defaults
startResponse = 0
currentSymbol = 1

# Constants
SYMBOLS = ["-","X", "O"]

# 0 for empty; 1 = X; 2 = O
GAME_BOARD = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def show_start(errorMsg = None):
    clear_console()

    if errorMsg:
        print("\n"+"="*20, f"\n {errorMsg}", "\n" + "="*20, "\n")

    print("="*10 + " TIC TAC TOE " + "="*10, "\n")
    print(" " * 2 + "1. START GAME", "\n")
    startResponse = input("-> Select an option: ")

    # Tries to parse received input to integer
    parsedResponse = 0 if not startResponse.isdigit() else int(startResponse)

    return parsedResponse

def draw_board(board=GAME_BOARD):
    clear_console()

    for yIndex in range(0, 3):
        print("\n", end=" "*5)
        for xIndex in range(0,3):

            positionValue = board[yIndex][xIndex]

            print(SYMBOLS[positionValue], end=" ")

    print("\n")

def play():
    global currentSymbol

    while True:
        draw_board()

        # Player index input
        selectedIndex = int(input("")) - 1

        # Converting to matrix position
        xIndex = selectedIndex // 3
        yIndex = selectedIndex % 3

        # Plays in the selected index
        GAME_BOARD[xIndex][yIndex] = currentSymbol

        # Flips the current player symbol
        currentSymbol = 3 - currentSymbol

def main(errorMsg=None):

    # Get selected mode
    startResponse = show_start(errorMsg if errorMsg else None)

    # Normal mode
    if startResponse == 1:
        play()
    else:
        # Fallback to start screen
        main("INVALID OPTION!")

if __name__ == "__main__":
    main()