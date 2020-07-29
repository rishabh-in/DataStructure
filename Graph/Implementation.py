class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + " is connected to: " + str([x.id for x in self.connectedTo])

class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertex = 0

    def addVertex(self, key):
        self.numVertex += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = Vertex(f)
        if t not in self.vertList:
            nv = Vertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(5):
    g.addVertex(i)

print(g.vertList)
print("\n")

g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(0, 4, 1)
g.addEdge(1, 2, 2)

for val in g:
    print(val)
    print(val.getConnections())
    print("\n")
