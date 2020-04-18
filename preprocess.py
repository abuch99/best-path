import urllib.parse
import configparser
import json as JSON
from os import path
from helpers import geoloc,openFiles,distanceMatrix
from graph import Graph

config = configparser.ConfigParser()
config.read('config.ini')
key=config['bing']['key']

def nodeList(nodes):
    nodedict=dict()
    if not path.exists('dict.json'):
        for item in nodes:
            urllib.parse.quote(item)
            url='http://dev.virtualearth.net/REST/v1/Locations?query='+item+'&key='+key
            nodedict[item]=geoloc(url)

        json = JSON.dumps(nodedict)
        f = open("dict.json","w")
        f.write(json)
        f.close()

    else:
        with open('dict.json', 'r') as f:
            nodedict=JSON.load(f)

    return nodedict

def durationList(nodes, nodedict):
    if not path.exists('duration.json'):
        sendurl='https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key='+key
        matrix=distanceMatrix(sendurl, nodedict)
        durations={}
        for name,time in zip(nodes, matrix):
            durations[name]=time

        json = JSON.dumps(durations)
        f = open("duration.json","w")
        f.write(json)
        f.close()

    else:
        with open('duration.json', 'r') as f:
            durations=JSON.load(f)
    
    return durations

def init():
    data=openFiles()
    nodes = data[0]
    edges = data[1]
    nodedict = nodeList(nodes)
    durations = durationList(nodes,nodedict)

    return (nodes, edges, nodedict, durations)