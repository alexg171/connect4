class DecisionTree:
    def __init__(self, root):
        self.root = root
        self.children = []
        self.bestmove = root
        self.movewhere = -1
    def getBestMove(self, node, level, currentlvl, parents):
        if(currentlvl == level and self.bestmove.getMove() != -1):
            if(node.getBoard().isEqual(self.bestmove.getBoard()) and len(parents) > 0):
                #self.printParentList(parents)
                #print()
                self.movewhere = parents[0].getMove()
        for child in node.getChildren():
            if child.getRating() > self.bestmove.getRating():
                self.bestmove = child
                parents.append(child)
            self.getBestMove(child, level, currentlvl+1, parents)
    def printParentList(self, list):
        for elem in list:
            print(elem.getMove(), end=" ")
    def getRoot(self):
        return self.root
    def generateTree(self, node, level, currentlvl):
        if currentlvl > level:
            return
        else:
            for i in range(node.board.getColumns()):
                if i not in node.board.getFullColumns():
                    newboard = node.board
                    newboard.drop(i,2)
                    child = DecisionNode(i,newboard)
                    #print("Move to column", child.move)
                    #print("Rating is:" , child.rating)
                    #child.board.print()
                    self.generateTree(child,level,currentlvl+1)
                    #print("")
                    node.addChild(child)


        return 1


class DecisionNode:
    def __init__(self, move, board):
        self.move = move
        self.board = board
        self.children = []
        self.rating = board.countNumInRow(3, 2)
    def getMove(self):
        return self.move
    def getRating(self):
        return self.rating
    def getBoard(self):
        return self.board
    def addChild(self, node):
        self.children.append(node)
    def getChildren(self):
        return self.children