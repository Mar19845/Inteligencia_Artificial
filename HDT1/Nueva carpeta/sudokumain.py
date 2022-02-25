from cleaner import *
from sudoku import *
print("****IA SUDOKU****\n")
st = True
f = '4.txt'



while(st):
    dim = input("Elija la dimension del sudoku que desea que la IA resuelva (UNICAMENTE 4,6 ó 9): ")

    if dim == "4":
        print("\n SUDOKU 4X4 \n")
        fileCleaner(f)
    elif dim == "6":
        print("\n SUDOKU 6X6 \n")
        fileCleaner(f)
    elif dim == "9":
        print("\n SUDOKU 9X9 \n")
        fileCleaner(f)
    else:
        print("¡Opcion invalida, intente de nuevo!")
        st1 = False