from pieceUtils import PieceUtils
from gridUtils import GridUtils
import sys

# Read STDIN and Parse Each Testcase String into Separate Lists
raw_game = sys.stdin.readlines()
games = []
for game in games:
    game = game.strip()
    game = game.split(",")
    games.append(game)
    print(game)

# Instantiate Grid Representation
gridUtils = GridUtils()

# Instantiate Piece Representation
pieceUtils = PieceUtils()

# Execute Tetris Game
for seq in games:
    # Play Testcase
    for move in seq:
        # Place Piece in Grid
        pass

# Write Solution to STDOUT
# We Want to Return the Tallest Height of each Testcase
# Use sys.stdout.write() or can try seeing what print does since that outputs to STDOUT