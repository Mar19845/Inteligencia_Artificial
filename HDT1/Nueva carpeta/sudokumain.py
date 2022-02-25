from cleaner import *
from sudoku import *
print("****IA SUDOKU****\n")
st = True
f = '4.txt'



while(st):
    dim = input("Elija la dimension del sudoku que desea que la IA resuelva (UNICAMENTE 4,6 ó 9): ")

    if dim == "4":
        import sudoku4x4 as sdk4
        print("\n SUDOKU 4X4 \n")
        matrisLista =  fileCleaner(f) 
        print("________________")
        print("  ") 
        print("Solucion con Backtracking Algorithm") 
        print("  ") 
       # print("Esta importa", matrisLista)
        if (sdk4.Suduko(matrisLista, 0, 0)):
            sdk4.puzzle(matrisLista)
        else:
            print("Solution does not exist:(")
        print("  ")
        print("Success!") 
    elif dim == "6":
        import sudoku6x6 as sdk6
        print("\n SUDOKU 6X6 \n")
        matrisLista =  fileCleaner(f) 
        print("________________")
        print("  ") 
        print("Solucion con Backtracking Algorithm") 
        print("  ")
        if (sdk6.Suduko(matrisLista, 0, 0)):
                sdk6.puzzle(matrisLista)
        else:
            print("Solution does not exist:(")
        print("  ")
        print("Success!") 
    elif dim == "9":
        import sudoku9x9 as sdk9
        print("\n SUDOKU 9X9 \n")
        matrisLista =  fileCleaner(f) 
        print("________________")
        print("  ") 
        print("Solucion con Backtracking Algorithm") 
        print("  ")
       # print("Esta importa", matrisLista)
        if (sdk9.Suduko(matrisLista, 0, 0)):
            sdk9.puzzle(matrisLista)
        else:
            print("Solution does not exist:(")
        print("  ")
        print("Success!")
    else:
        print("¡Opcion invalida, intente de nuevo!")
        st1 = False