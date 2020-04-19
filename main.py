from pyfiles.graph import Graph
from pyfiles.preprocess import init,durationList
from pyfiles.aStar import aStar
from pyfiles.helpers import mapNodes

data=init()
nodes=data[0]
edges=data[1]
nodedict=data[2]

g=Graph()
for item in edges:
    g.addEdge(item)

g_edges = g.getEdges()
durations = durationList(nodes,nodedict, g_edges)

# for key,value in durations.items():
#     print(str(key) + ' | ' + str(value))
for items in nodes:
    durations[(items,items)]=0
start='Birla Institute of Technology Hyderabad'
end='RGIA'

path = aStar(g,nodedict,durations,start,end)

print('PATH')
print('****************************')
for item in path:
    print (item)
print('****************************')
print()
# with open('path.txt','w') as f:
#     for item in path:
#         f.write(str(item))
#         f.write("\n")
mapNodes(path,nodedict)