import urllib.parse
import configparser
import json as JSON
from os import path
from helpers import geoloc,openFiles,durationMatrix
from graph import Graph
import pickle


def nodeList(nodes):
    nodedict=dict()
    if not path.exists('dict.json'):
        for item in nodes:
            urllib.parse.quote(item)   
            nodedict[item]=geoloc(item)

        json = JSON.dumps(nodedict)
        f = open("dict.json","w")
        f.write(json)
        f.close()

    else:
        with open('dict.json', 'r') as f:
            nodedict=JSON.load(f)

    return nodedict

def durationList(nodes, nodedict, g_edges):
    if not path.exists('durationsPickle'):
        durations={}
        for start,end in g_edges:
            print(start+'|')    
            print(end)
            matrix=durationMatrix(nodedict, start, end)  
            t=(start,end)          
            durations[t]=matrix[0]
            # print(durations)
        
        for item in nodes:         
            if item=='RGIA':
                continue

            end = "RGIA"
            start=item
            matrix=durationMatrix(nodedict, start, end)  
            t=(start,end)          
            durations[t]=matrix[0]
            matrix=durationMatrix(nodedict, end, start)
            t=(end,start)          
            durations[t]=matrix[0]

        dbfile = open('durationsPickle', 'ab')
        pickle.dump(durations, dbfile)
        dbfile.close()

    else:
        dbfile = open('durationsPickle', 'rb')
        durations = pickle.load(dbfile)
    
    return durations

def init():
    data=openFiles()
    nodes = data[0]
    edges = data[1]
    nodedict = nodeList(nodes)
    return (nodes, edges, nodedict)