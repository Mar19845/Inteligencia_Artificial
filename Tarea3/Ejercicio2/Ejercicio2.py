import numpy as np
from itertools import combinations
def TSP_SA(G):
    s = list(range(len(G)))
    c = cost(G, s)
    ntrial = 1
    T = 30
    alpha = 0.99

    while ntrial <= 1000:
      n = np.random.randint(0, len(G))
      while True:
         m = np.random.randint(0, len(G))
         if n != m:
            break
      s1 = swap(s, m, n)
      c1 = cost(G, s1)
      if c1 < c:
         s, c = s1, c1
      else:
         if np.random.rand() < np.exp(-(c1 - c)/T):
            s, c = s1, c1
      T = alpha*T
      ntrial += 1

def swap(s, m, n):
   i, j = min(m, n), max(m, n)
   s1 = s.copy()
   while i < j:
      s1[i], s1[j] = s1[j], s1[i]
      i += 1
      j -= 1
   return s1
 
def cost(G, s):
   l = 0
   for i in range(len(s)-1):
      l += G[s[i]][s[i+1]]
   l += G[s[len(s)-1]][s[0]] 
   return l


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
