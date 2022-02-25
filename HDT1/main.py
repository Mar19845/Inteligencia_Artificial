
from grafo import *
from helpers import *
comp = True

while comp:
    opt = input("Ingrese 1 para resolver o 2 para salir: ")
    if opt == '1':
        archvio = input("Ingrese el nombre del archivo con el grafo: ")
        start = input("Ingrese el punto inicial: ")
        end = input("Ingrese el punto final: ")
        
        n,m,aristas = read_file(archvio)
        _,nodes = create_graph(aristas)
        G = Graph()
        G.addNodes(nodes)
        G.addEdges(aristas)
        distance_value, path_s_e = dijkstra(G,start,end)
        
        print('Del punto inicial ',start,' al punto final ',end,' el camino mas corto es de: ', distance_value)
        print('El camino a seguir es por los nodos: ',path_s_e)
    if opt == '2':
        comp = False