class Tree:
    nodes = []
    deep = 0

    def __init__(self, nodes, deep):
        self.nodes = nodes
        self.deep = deep

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