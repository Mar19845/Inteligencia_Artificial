from cleaner import *

print("****IA SUDOKU****\n")
st = True
f = "4dms.txt"
f1 = "6dms.txt"
f2 = "9dms.txt"

while(st):
    dim = input("Elija la dimension del sudoku que desea que la IA resuelva (UNICAMENTE 4,6 ó 9): ")

    if dim == "4":
        fileCleaner(f)
    elif dim == "6":
        fileCleaner(f1)
    elif dim == "9":
        fileCleaner(f2)
    else:
        print("¡Opcion invalida, intente de nuevo!")
        st1 = False