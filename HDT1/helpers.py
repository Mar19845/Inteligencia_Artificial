
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
        results = list(map(int, line.split(',')))
        #append results list to aristas
        aristas.append(results)
        
        
    return n, m, aristas


print(*read_file('grafo.txt'))