import array as arr
#
class PieceUtils:
    
    def __init__(self):
        # Key: pieceLetter -> Value: Elementary coords Piece's 4 blocks (based on (0,0) origin)
        coordMap = {}
        coordMap.update({"Q": [[0,0],[0,1],[1,0],[1,1]]})
        coordMap.update({"Z": [[0,1],[1,0],[1,1],[2,0]]})
        coordMap.update({"S": [[0,0],[1,0],[1,1],[2,1]]})
        coordMap.update({"T": [[0,1],[1,0],[1,1],[2,1]]})
        coordMap.update({"I": [[0,0],[1,0],[2,0],[3,0]]})
        coordMap.update({"L": [[0,0],[1,0],[0,1],[0,2]]})
        coordMap.update({"J": [[0,0],[1,0],[1,1],[1,2]]})
        self.pieceCoords = coordMap
        # Key: pieceLetter -> Value: height
        heightsMap = {}
        heightsMap.update({"Q":2})
        heightsMap.update({"Z":2})
        heightsMap.update({"S":2})
        heightsMap.update({"T":2})
        heightsMap.update({"I":1})
        heightsMap.update({"L":3})
        heightsMap.update({"J":3})
        self.pieceHeights = heightsMap
        # Key: pieceLetter -> Value: width
        widthsMap = {}
        widthsMap.update({"Q":2})
        widthsMap.update({"Z":3})
        widthsMap.update({"S":3})
        widthsMap.update({"T":3})
        widthsMap.update({"I":4})
        widthsMap.update({"L":2})
        widthsMap.update({"J":2})
        self.pieceWidths = widthsMap

    def getPieceCoords(self, pieceLetter):
        return self.pieceCoords[pieceLetter]

    def getPieceWidth(self, pieceLetter):
        return self.pieceHeights[pieceLetter]

    def getPieceHeight(self, pieceLetter):
        return self.pieceWidths[pieceLetter]