from anytree import Node, RenderTree

class TreesGenerator:
    _treePossibleNumber = Node("0")
    _treeNoPossibleNumber = Node("1")

    def __init__(self, answers):
        self.generateTrees(answers)

    def generateTrees(self, answers):
        self._initTreePossibleNumber(answers)
        self._initTreeNoPossibleNumber(answers)

        return [self._treePossibleNumber, self._treeNoPossibleNumber]

    def addFromNumberPosition(self, position, number, father):

        if position > 0:
            for i in range(1, 10):
                leaf = Node(str(i), father)
                self.addFromNumberPosition(position - 1, number, leaf)
        else:
            Node(str(number), father)

    def addFromBoundariesWithValues(self, values, tree):
        if len(values) > 0:
            for i in range(values.pop(0), 9):
                subTree = Node(str(i), tree)
                self.addFromBoundariesWithValues(subTree)
        else:
            print("")


    def addFromBoundariesToTree(self, signal, value, tree):

        listOfSplittedValues = [int(i) for i in str(value)]

        if signal == ">":
            self.addFromBoundariesWithValues(listOfSplittedValues, tree)

        if signal == "<":
            print("sss")

    def addFromBoundaries(self, answers, tree):

        if answers[4] == "1":
            self.addFromBoundariesToTree("<", answers[3], tree)
        else:
            self.addFromBoundariesToTree(">", answers[3], tree)

        if answers[6] == "1":
            self.addFromBoundariesToTree(">", answers[5], tree)
        else:
            self.addFromBoundariesToTree("<", answers[5], tree)

    def _initTreePossibleNumber(self, answers):

        # Generate tree of possible number
        # Using the position and number
        self.addFromNumberPosition(answers[1], answers[2], self._treePossibleNumber)

        # Using boundaries defined by the user
        self.addFromBoundaries(answers, self._treePossibleNumber)


    def _initTreeNoPossibleNumber(self, answers):
        # Generate tree of no possible numbers

        print("aaaa")
