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
    data_origin=[]
    data_dest=[]
    jsondata = {}
    for key in nodedict:
        temp={}
        if key == 'RGIA':
            temp['latitude']=nodedict[key][0]
            temp['longitude']= nodedict[key][1]
            data_dest.append(temp)
        else:
            temp['latitude']=nodedict[key][0]
            temp['longitude']=nodedict[key][1]
            data_origin.append(temp)

    jsondata['origins']=data_origin
    jsondata['destinations']=data_dest
    jsondata['travelMode']='driving'
    jsondata=json.dumps(jsondata)
    return jsondata

def distanceMatrix(sendurl,nodedict):
    jsondata=getjson(nodedict)   
    r = requests.post(url=sendurl, data=jsondata)
    try:
        j=json.loads(r.text)
        distances=[]
        try:
            loc = j['resourceSets'][0]['resources'][0]['results']
            for item in loc:
                distances.append(item['travelDuration'])
            return(((distances)))
        except ValueError:
            print("Wrong")
    except ValueError:
        print("Wrong")

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