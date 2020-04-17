import csv
import urllib.parse
import requests
import json 

nodes = []
edges = []
places = "places.csv"
conn = "edges.csv"

def geoloc(sendurl):
    r=requests.get(sendurl)
    try:
        j=json.loads(r.text)
        try:
            loc = j['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']
            return(tuple(loc))
        except ValueError:
            print("Wrong")
    except ValueError:
        print("Wrong")
    return []

def getjson(nodedict):
    data=[]
    jsondata = {}
    for key in nodedict:
        temp={}
        if key == 'RGIA':
            temp['latitude']=nodedict[key][0]
            temp['longitude']= nodedict[key][1]
            jsondata['destinations']=temp
        else:
            temp['latitude']=nodedict[key][0]
            temp['longitude']=nodedict[key][1]
            data.append(temp)

    jsondata['origins']=data
    json.dumps(jsondata)
    return jsondata

def distanceMatrix(nodedict):
    jsondata=getjson(nodedict)    

def openFiles():
    with open(places, encoding='utf-8-sig') as fileplace:
        placereader=csv.reader(fileplace)

        for place in placereader:
            place=''.join(place)
            nodes.append((place))

    with open(conn, encoding='utf-8-sig') as fileconn:
        connreader=csv.reader(fileconn)
        for edge in connreader:
            edges.append(edge)

    return [nodes,edges]