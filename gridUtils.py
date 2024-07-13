import copy
#
class GridUtils:

    # Instantiate Grid in Constructor
    # Will Use 1's and 0's (0=Empty, 1=Occupied)
    # Default Starting Size Dimensions Will Be 10 rows x 5 columns
    # Game Grid Representation is Sideways:
    #   Pieces will be "dropped" from right to left (Col 0 = Bottom Row)
    def __init__(self):
        self.gridObject = [[0]*5 for _ in range(10)]
        self.maxHeightOfCols = [0] * 10
        self.gridHeight = 5
    
    def placePiece(self, wOffset, pieceLetter, pieceCoords, pieceUtils):
        # Grab Piece Coordinates form params
        # --> offset coordinates based on moveCol specified in move
        offsetCoords = copy.deepcopy(pieceCoords)
        print("Coords before width offset: ", offsetCoords)
        for i in range(4):
            offsetCoords[i][0] += wOffset
        print("Coords after width offset: ", offsetCoords)
        # Check the heights against the topmost occupied column heights (see if exceeds height of grid)
        #   (use width to note the columns you'll be checking? might just need to iterate through the coords w/o needing to grab width)
        #   if height addition exceeds height of grid, double the height of each "column" 
        #   (can check if len(row)-PieceHeigth <= col height for each column as an alternative)
        for coord in offsetCoords:
            # print(coord[0])
            # print(self.maxHeightOfCols[coord[0]])
            # TODO: Investigate why this gives out of bounds error in some cases
            if self.gridHeight < pieceUtils.getPieceHeight(pieceLetter) + self.maxHeightOfCols[coord[0]]:
                self.growGridHeight()
                break
        # Determine the minDiff of the related columns for the piece's squares
        # TODO: Figure out why the hoffset is incorrect
        hOffset = self.findHeightOffset(offsetCoords, pieceUtils.getPieceHeight(pieceLetter))
        print("hOffset: ", hOffset)
        # offset piece based on the minDiff
        print("Coords before height offset: ", offsetCoords)
        for i in range(4):
            offsetCoords[i][1] += hOffset
            # set new max height in a column if height of piece's square is > the current max height in the column
            if offsetCoords[i][1] > self.maxHeightOfCols[offsetCoords[i][0]]:
                # TODO: Added +1 for now because need to investigate if maxHeightOfCols is being tracked as index or height value
                # This might be the correct move and all we need to do is adjust the maxHeightOfCols correctly after shifting rows
                self.maxHeightOfCols[offsetCoords[i][0]] = offsetCoords[i][1] + 1
        print("maxHeightOfCols after offset: ", self.maxHeightOfCols)
        print("Coords after height offset: ", offsetCoords)
        
        for coord in offsetCoords:
            self.gridObject[coord[0]][coord[1]] = 1
        
        # -------- (From here below) need to determine whether want to separate these actions into tetris.py or put in this placePiece func)
        # Scan the grid for full row(s)
        # Adjust the rows
        # Update the maxHeightOfCols List (maybe just update it as we place pieces instead)

    # Doubling height would cost less time in long run for longer testcases
    def growGridHeight(self):
        """
        - Doubles the 'height' of the grid
        - Updates gridHeight
        """
        # TODO: Investigate if extend is truly working (seems like the size is expanding at least)
        for i in range(10):
            self.gridObject[i].extend([0]*self.gridHeight)
        self.gridHeight *= 2

    def findHeightOffset(self, coords, pieceHeight):
        # uses min difference between a coordinate and the max height of the relative "columns" to return height offset from "bottom"
        # this will determine the placement in the "height" axis
        # TODO: Instead of returning an hOffset, let's use the maxHeightOfCols to determine the offset
        minDiff = self.gridHeight
        minDiffCol = 0
        print("Grid Height While Finding hOffset: ", minDiff)
        for i in range(4):
            # TODO: Fix Criteria for assigning minDiff
            if self.gridHeight - self.maxHeightOfCols[coords[i][0]] < minDiff:
                minDiff = self.gridHeight - self.maxHeightOfCols[coords[i][0]]
                minDiffCol = coords[i][0]
        return self.maxHeightOfCols[minDiffCol]

    def getColMaxHeights(self):
        return self.maxHeightOfCols

    # def updateColMaxHeights(self):
    #     """
    #     Update the highest heights in each column in maxHeightOfCols list
    #     """
    #     pass

    def findFullRow(self):
        """
        - Scan grid for a full row from bottom up
        - return heightIdx for first full row found, otherwise return -1
        """
        for i in range(self.gridHeight):
            row = [self.gridObject[j][i] for j in range(10)]
            if row == [1]*10:
                return i
            
        return -1
    
    # Use to Shift Rows if a Full Row is Found
    def shiftRows(self, start):
        """
        Clear the level 'start',  then shift every  row down by 1
        """
        # shift everything down by one above the full row (execute this operation above each full row, starting with bottom-most level)
        print("Grid Object Before Shifting Rows: ")
        for row in self.getGridObject():
            print(row)
        self.clearRow(start)
        for i in range(start, self.gridHeight-1):
            for j in range(10):
                # TODO: Investigate why this is giving the 'int' object is not subscriptable ERROR
                nextVal = self.gridHeight[j][i+1]
                self.gridHeight[j][i] = nextVal
                # adjust max col height if necessary
                if i == self.maxHeightOfCols[j]:
                    self.maxHeightOfCols[j] -= 1

    def clearRow(self, heightIdx):
        """
        Sets a 'row' to all 0's
        """
        for i in range(10):
            self.gridObject[i][heightIdx] = 0

    def clearGrid(self):
        self.gridObject = [[0]*5 for _ in range(10)]
        self.gridHeight = 5

    def getGridObject(self):
        return self.gridObject