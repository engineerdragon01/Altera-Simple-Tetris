class PieceUtils():

    def __init__(self):
        self.pieces = {
    'Q': [[1, 1],
          [1, 1]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'T': [[1, 1, 1],
          [0, 1, 0]],
    'I': [[1, 1, 1, 1]],
    'L': [[1, 0],
          [1, 0],
          [1, 1]],
    'J': [[0, 1],
          [0, 1],
          [1, 1]],
    }
        
    def getPiece(self, pieceLetter):
        return self.pieces.get(pieceLetter)