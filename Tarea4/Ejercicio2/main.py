from helpers import *
import time
inicio = time.time()

#Create a sudoku 
# pass data for the genetic algorithm 
sudoku = Sudoku(
        number_of_candidates=500,
        number_of_elites=80,
        number_of_generations=1000,
        number_of_mutations=0,
        selection_rate=0.85
    )

#load the sudoku from a file 
sudoku.load('input.txt')

#save the solution
solution = sudoku.solve()

if solution:
    #save the solution in a txt file
    sudoku.save('output.txt', solution)

print("tiempo de ejecucion: ")
fin = time.time()
print(fin-inicio)