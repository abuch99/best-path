class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        edges=[]
        for key,value in self.gdict.items():
            for node in value:
                temp=(key,node)
                edges.append(temp)
        return edges

    def addEdge(self, edge):
            edge = set(edge)
            (v1, v2) = tuple(edge)
            if v1 in self.gdict:
                self.gdict[v1].append(v2)
            elif v1 not in self.gdict:
                self.gdict[v1] = [v2]
            if v2 not in self.gdict:
                self.gdict[v2] = []

