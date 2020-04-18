import csv
import urllib.parse
import requests
import json 
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
key=config['bing']['key']

nodes = []
edges = []
places = "places.csv"
conn = "edges.csv"

def geoloc(item):
    sendurl='http://dev.virtualearth.net/REST/v1/Locations?query='+item+'&key='+key
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

def getjson(nodedict, start=False, dest=False):
    data_origin=[]
    data_dest=[]
    jsondata = {}
    
    temp={}
    temp['latitude']=nodedict[dest][0]
    temp['longitude']= nodedict[dest][1]
    data_dest.append(temp)

    temp={}
    temp['latitude']=nodedict[start][0]
    temp['longitude']=nodedict[start][1]
    data_origin.append(temp)

    jsondata['origins']=data_origin
    jsondata['destinations']=data_dest
    jsondata['travelMode']='driving'
    jsondata=json.dumps(jsondata)
    return jsondata

def durationMatrix(nodedict, start=False,dest=False):
    sendurl='https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key='+key
    jsondata=getjson(nodedict,start,dest)   
    # print(jsondata)
    r = requests.post(url=sendurl, data=jsondata)
    try:
        j=json.loads(r.text)
        durations=[]
        try:
            loc = j['resourceSets'][0]['resources'][0]['results']
            for item in loc:
                durations.append(item['travelDuration'])
                print(durations)
            return(((durations)))
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

    return (nodes,edges)