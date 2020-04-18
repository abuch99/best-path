from graph import Graph
from preprocess import init,durationList
from aStar import aStar

data=init()
nodes=data[0]
edges=data[1]
nodedict=data[2]


g=Graph()
for item in edges:
    g.addEdge(item)

g_edges = g.getEdges()
print(len(g_edges))
durations = durationList(nodes,nodedict, g_edges)

start='Birla Institute of Technology Hyderabad'
end='RGIA'

# path = aStar(g,nodedict,durations,start,end)