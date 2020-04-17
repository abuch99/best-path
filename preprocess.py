import csv
import urllib.parse

key = 'AimWj22Gy9mlEX040aIzrEMn_bmPx3opQEGedCL6EZYbXDdQ10i3fvmQTajYIlMN'
nodes = []
edges = []

places = "places.csv"
conn = "edges.csv"

with open(places, 'r') as fileplace:
    placereader=csv.reader(fileplace)

    for place in placereader:
        nodes.append(place)

with open(conn, 'r') as fileconn:
    connreader=csv.reader(fileconn)

    for edge in connreader:
        edges.append(edge)

test = nodes[0]
urllib.parse.quote(test)
url = 'http://dev.virtualearth.net/REST/v1/Locations?countryRegion=India&locality=Hyderabad&addressLine={test}&userLocation=17.387140,78.491684&userIp={userIp}&key='+key


nodedict=[]

for item in nodes:
