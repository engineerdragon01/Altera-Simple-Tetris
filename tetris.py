from pieceUtils import PieceUtils
import sys

def validPlacement(grid, piece, startRow, startCol):
    """
    Returns whether a piece can be placed at the specified position
    - grid: List[List[int]] = grid matrix representation
    - piece: List[List[int]] = piece matrix representation
    - startRow: int = specified row coordinate to start checking from
    - startCol: int = specified col coordinate to start checking from
    """
    rows, cols = len(grid), len(grid[0])
    pieceRows, pieceCols = len(piece), len(piece[0])
    
    for i in range(pieceRows):
        for j in range(pieceCols):
            if piece[i][j] == 1:
                if startRow + i >= rows or startCol + j < 0 or startCol + j >= cols:
                    return False
                if grid[startRow + i][startCol + j] == 1:
                    return False
    return True

def placePiece(grid, piece, startRow, startCol):
    """
    Places piece into the grid AND grows the 'height' of the grid when running out of space
    - grid: List[List[int]] = grid matrix representation
    - piece: List[List[int]] = piece matrix representation
    - startRow: int = specified row coordinate to start placing piece matrix
    - startCol: int = specified col coordinate to start placing piece matrix
    """
    pieceRows, pieceCols = len(piece), len(piece[0])
    
    for i in range(pieceRows):
        for j in range(pieceCols):
            if piece[i][j] == 1:
                if startRow + i >= len(grid):
                    grid.append([0] * len(grid[0]))
                grid[startRow + i][startCol + j] = 1

def clearFullRows(grid):
    """
    Creates new grid object that excludes full rows, then fills top with empty rows
    - grid: List[List[int]] = grid matrix representation
    """
    newGrid = [row for row in grid if not all(cell == 1 for cell in row)]
    num_full_rows = len(grid) - len(newGrid)
    
    for _ in range(num_full_rows):
        newGrid.insert(0, [0] * len(grid[0]))
    
    return newGrid

def dropPiece(grid, piece, startCol):
    """
    Drops piece into the grid from top at the startCol position
    - grid: List[List[int]] = grid matrix representation
    - piece: List[List[int]] = piece matrix representation
    - startCol: int = left-most column position that piece will start dropping from
    """
    rows = len(grid)
    pieceRows = len(piece)
    
    for row in range(rows - pieceRows + 1):
        if not validPlacement(grid, piece, row, startCol):
            placePiece(grid, piece, row - 1, startCol)
            grid = clearFullRows(grid)
            return grid
    
    placePiece(grid, piece, rows - pieceRows, startCol)
    grid = clearFullRows(grid)
    
    return grid

def executeGame(game, pieceUtils):
    """
    Initialize an empty grid, execute moves in game, and return the maxHeight of the game grid
    - game: List[str] = list of moves formatted as pieceType + startCol (i.e. "Q0")
    - pieceUtils: PieceUtils = object used to obtain piece matrix representations
    """
    grid = [[0] * 10 for _ in range(10)]

    for move in game:
        pieceType = move[0]
        startCol = int(move[1])
        piece = pieceUtils.getPiece(pieceType)
        grid = dropPiece(grid, piece, startCol)

    height = len(grid) - next((i for i, r in enumerate(grid) if any(r)), len(grid))
    return height

pieceUtils = PieceUtils()

raw_game = sys.stdin.readlines()
games = []
for game in raw_game:
    game = game.strip()
    game = game.split(",")
    games.append(game)

for g in games:
    maxHeight = executeGame(g, pieceUtils)
    sys.stdout.write(f"{maxHeight}\n")