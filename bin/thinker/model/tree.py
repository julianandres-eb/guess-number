import bin.thinker.model.node as nd

class Tree:

    nodes = nd.Node([], 0, 0)
    actualDeep = 0
    maxDeep = 0

    def __init__(self, nodes, actualDeep, maxDeep):
        self.nodes = nodes
        self.actualDeep = actualDeep
        self.maxDeep = maxDeep

    # def addNodes
    # def deleteNodes
    # podar con cierto valor para abajo

    def setNodes(self, nodes):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

    def setDeep(self, deep):
        self.deep = deep

    def getDeep(self):
        return self.deep

    def setMaxDeep(self, maxDeep):
        self.maxDeep = maxDeep

    def getMaxDeep(self):
        return self.maxDeep