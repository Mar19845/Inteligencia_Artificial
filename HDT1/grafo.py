from collections import defaultdict
from turtle import distance
from helpers import *

inf = float('inf')


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNodes(self,list_nodes):
        for node in list_nodes:
            self.nodes.add(node)
    
    def addEdges(self,aristas):
        for arista in aristas:
            self.edges[arista[0]].append(arista[1])
            self.distances[(arista[0], arista[1])] = arista[2]
'''
n,m,aristas = read_file('grafo.txt')
_,nodes = create_graph(aristas)

G = Graph()
G.addNodes(nodes)
G.addEdges(aristas)
#print(G.nodes)
#print(G.edges)
#print(G.distances)
'''

def dijkstra(graph, initial,end):
    vecino = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in vecino:
                if minNode is None:
                    minNode = node
                elif vecino[node] < vecino[minNode]:
                    minNode = node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight = vecino[minNode]
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in vecino or weight < vecino[edge]:
                vecino[edge] = weight
                path[edge].append(minNode)
    
    
    camino = [end]
    if vecino[end] < inf:
        while initial not in camino:
            last_index = camino[-1]
            val = path[last_index]
            camino.append(val[0])
    distancia = vecino[end]
    return distancia,camino
'''
print(dijkstra(G,'1','5'))

import networkx as nx
n,m,aristas = read_file('grafo.txt')
G = nx.Graph()
G.add_weighted_edges_from(aristas)

print('-----------------------')
print(nx.dijkstra_path(G,'1','5'))
print(nx.dijkstra_path_length(G,'1','5'))
'''
