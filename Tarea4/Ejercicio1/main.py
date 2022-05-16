from random import randint
from helpers import *

#max number of iterations
INT_MAX = 2147483647
#number of cities
V = 5
# Names of the cities
GENES = "ABCDE"
# Starting Node Value
START = 0
# Initial population size for the algorithm
POP_SIZE = 10


# Utility function for TSP problem.
def TSPUtil(mp):
    file = open("result.txt","w+")
    # Generation Number
    gen = 1
    # Number of Gene Iterations
    gen_thres = 5
    population = []
    temp = individual()
    #list of lines to be written on a txt
    lines = []
    # Populating the GNOME pool.
    for i in range(POP_SIZE):
        temp.gnome = create_gnome(V)
        temp.fitness = cal_fitness(temp.gnome,INT_MAX)
        population.append(temp)
    #write in file
    file.write("\nInitial population: \nGNOME     FITNESS VALUE\n")
    for i in range(POP_SIZE):
        #write in file
        string = ""+str(population[i].gnome) + " " + str(population[i].fitness) + "\n"
        file.write(string)
        
    found = False
    temperature = 10000
    # Iteration to perform
    # population crossing and gene mutation.
    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        #write in file
        string = "\nCurrent temp: "+str(temperature) + "\n"
        file.write(string)
        #list og the new population
        new_population = []
        for i in range(POP_SIZE):
            p1 = population[i]
            while True:
                new_g = mutatedGene(p1.gnome,V)
                new_gnome = individual()
                new_gnome.gnome = new_g
                new_gnome.fitness = cal_fitness(new_gnome.gnome,INT_MAX)
                if new_gnome.fitness <= population[i].fitness:
                    new_population.append(new_gnome)
                    break
                else:
                    # Accepting the rejected children at
                    # a possible probability above threshold.
                    prob = pow(
                        2.7,
                        -1
                        * (
                            (float)(new_gnome.fitness - population[i].fitness)
                            / temperature
                        ),
                    )
                    if prob > 0.5:
                        new_population.append(new_gnome)
                        break
        temperature = cooldown(temperature)
        population = new_population
        #write in file
        string = "Generation: "+str(gen) +"\n"
        file.write(string)
        #write in file
        file.write("GNOME     FITNESS VALUE \n")
        for i in range(POP_SIZE):
            #write in file
            string = ""+str(population[i].gnome) + "\t" + str(population[i].fitness) + "\n"
            file.write(string)
        gen += 1
    
    #call writeng txt def function    
    file.close()
#list of list whith the cities map node
mp = [
        [0, 2, INT_MAX, 12, 5],
        [2, 0, 4, 8, INT_MAX],
        [INT_MAX, 4, 0, 3, 3],
        [12, 8, 3, 0, 10],
        [5, INT_MAX, 3, 10, 0],
    ]

TSPUtil(mp)