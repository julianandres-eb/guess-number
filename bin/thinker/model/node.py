class Node:
    nodes = []
    deep = 0
    currentValue = 0

    def __init__(self, nodes, deep, currentValue):
        self.nodes = nodes
        self.deep = deep
        self.currentValue = currentValue

    # def addNodes
    # def deleteNodes

    def setNodes(self, nodes):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

    def setDeep(self, deep):
        self.deep = deep

    def getDeep(self):
        return self.deep

    def setCurrentValue(self, cv):
        self.currentValue = cv

    def getCurrentValue(self):
        return self.currentValue