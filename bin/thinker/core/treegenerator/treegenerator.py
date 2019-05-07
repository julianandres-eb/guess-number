import bin.thinker.model.tree as tr
import bin.thinker.model.node as nd

class TreesGenerator:
    _treePossibleNumber = tr.Tree([], 0, 0)
    _treeNoPossibleNumber = tr.Tree([], 0, 0)

    def __init__(self, answers):
        self.generateTrees(answers)

    def generateTrees(self, answers):
        self._initTreePossibleNumber(answers)
        self._initTreeNoPossibleNumber(answers)

        return [self._treePossibleNumber, self._treeNoPossibleNumber]

    def _initTreePossibleNumber(self, answers):

        # Generate tree of possible number
        self._treePossibleNumber = tr.Tree([], 0, answers[0])

        # Using the number and position



    def _initTreeNoPossibleNumber(self, answers):
        # Generate tree of no possible numbers
        self._treePossibleNumber = tr.Tree([], 0, answers[0])
