from graph import Graph
from preprocess import init

data=init()
nodes=data[0]
edges=data[1]
nodedict=data[2]
durations=data[3]

g=Graph()
for item in edges:
    g.addEdge(item)

print(len(g.getEdges()))
