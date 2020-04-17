import urllib.parse
from helpers import geoloc,openFiles
from graph import Graph

key = 'AimWj22Gy9mlEX040aIzrEMn_bmPx3opQEGedCL6EZYbXDdQ10i3fvmQTajYIlMN'
data=openFiles()

nodes = data[0]
edges = data[1]

nodedict=dict()

for item in nodes:
    urllib.parse.quote(item)
    sendurl = 'http://dev.virtualearth.net/REST/v1/Locations?countryRegion=India&locality=Hyderabad&addressLine='+item+'&userLocation=17.387140,78.491684&key='+key
    nodedict[item]=geoloc(sendurl)

print (len(nodedict))

g=Graph()
for item in edges:
    g.addEdge(item)

print(len(g.getVertices()))