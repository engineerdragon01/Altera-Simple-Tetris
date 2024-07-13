from pieceUtils import PieceUtils
from gridUtils import GridUtils
import sys
import copy

# Read STDIN and Parse Each Testcase String into Separate Lists
raw_game = sys.stdin.readlines()
games = []
for game in raw_game:
    game = game.strip()
    game = game.split(",")
    games.append(game)

# Instantiate Grid Representation
gridUtils = GridUtils()

# Instantiate Piece Representation
pieceUtils = PieceUtils()

# Solution List
solutions = []

# Execute Tetris Game
for seq in games:
    # Play Testcase
    for move in seq:
        print("Move: ", move)
        # Determine Piece and Column
        movePiece = move[0]
        moveCol = int(move[1])

        moveCoords = pieceUtils.getPieceCoords(movePiece)
        print("Move Coordinates: ", moveCoords)
        # Place Piece in Grid
        gridUtils.placePiece(moveCol, movePiece, moveCoords, pieceUtils)
        print("Grid After Move: ")
        for row in gridUtils.getGridObject():
            print(row)
        print("MaxHeight before shift: ", max(gridUtils.getColMaxHeights()))

        # Scan grid for full rows and shift rows down accordingly
        fullRowIdx = 0
        while fullRowIdx >= 0:
            print("Grid Before Full Row Search: ")
            for row in gridUtils.getGridObject():
                print(row)
            fullRowIdx = gridUtils.findFullRow()
            print("Full Row Idx: ", fullRowIdx)
        # Adjust rows based on full row removal
            if fullRowIdx >= 0:
                gridUtils.shiftRows(fullRowIdx)
        # Update maxHeightOfCols list
        # gridUtils.updateColMaxHeights()
        print("----")
    print("|||||| Solution for this case: ", max(gridUtils.getColMaxHeights()))
    print("-------------------")
    # Save max height of testcase to solutions
    solutions.append(max(gridUtils.getColMaxHeights()))
    # Clear the Grid After Each TestCase
    gridUtils.clearGrid()

# Write Solution to STDOUT
# We Want to Return the Tallest Height of each Testcase
# Use sys.stdout.write() or can try seeing what print does since that outputs to STDOUT
for sol in solutions:
    sys.stdout.write(sol)
# print(solutions)
# print(gridUtils.getColMaxHeights())