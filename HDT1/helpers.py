
import numpy as np

def read_file(filename):
    #lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    n = int(lines[0])
    m = int(lines[1])
    #remove n and m from list
    lines.pop(0)
    lines.pop(0)
    
    #create list wiht the info of aristas
    aristas = []
    for line in lines:
        #split vaules in line and convert to int
        #results = list(map(int, line.split(',')))
        results = line.split(',')
        results[2] = int(results[2])
        #append results list to aristas
        aristas.append(results)
    
    #convert to np array
    #aristas = np.array(aristas)
    return n, m, aristas

def create_graph(aristas):
    graph = {}
    
    #agregar nodos al grafo
    for arista in aristas:
        graph[arista[0]] = {}
        graph[arista[1]] = {}
        #graph[arista[0]][arista[1]]=arista[2]
    
    #agregar las aristas a los nodoos, por cada nodo se crea un dict con key = al nodo que se dirige y el value es el peso
    for i in aristas:
        graph[i[0]][i[1]]=i[2]
    
    #return dict
    return graph, list(graph.keys())
