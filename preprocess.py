import urllib.parse
from helpers import geoloc,openFiles,getjson
from graph import Graph
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
key=config['bing']['key']

data=openFiles()

nodes = data[0]
edges = data[1]

nodedict=dict()

for item in nodes:
    urllib.parse.quote(item)
    sendurl = 'http://dev.virtualearth.net/REST/v1/Locations?countryRegion=India&locality=Hyderabad&addressLine='+item+'&userLocation=17.387140,78.491684&key='+key
    nodedict[item]=geoloc(sendurl)

g=Graph()
for item in edges:
    g.addEdge(item)


jsondata = getjson(nodedict)
json.dumps(jsondata)
print(jsondata)