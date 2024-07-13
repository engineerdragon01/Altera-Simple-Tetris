#
class PieceUtils:
    
    def __init__(self):
        # Initialize Dictionary with Key: pieceLetter -> Value: Elementary coords of piece's four blocks (from left to right, so bottom  pieces first)
        letterMap = {}
        letterMap.update({"Q": [(0,0),(0,0),(0,0),(0,0)]})
        letterMap.update({"Z": [(0,0),(0,0),(0,0),(0,0)]})
        letterMap.update({"S": [(0,0),(0,0),(0,0),(0,0)]})
        letterMap.update({"T": [(0,0),(0,0),(0,0),(0,0)]})
        letterMap.update({"I": [(0,0),(0,0),(0,0),(0,0)]})
        letterMap.update({"L": [(0,0),(0,0),(0,0),(0,0)]})
        letterMap.update({"J": [(0,0),(0,0),(0,0),(0,0)]})
        self.pieces = letterMap

    def getPieceOrientation(pieceLetter):
        pass

    def getPieceHeight(pieceLetter):
        pass