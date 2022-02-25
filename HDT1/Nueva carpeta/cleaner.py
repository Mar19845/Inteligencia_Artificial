import sudoku as sdk

def fileCleaner(txt):

    with open(txt) as file:
        lines = [line.rstrip() for line in file]

    n = lines[0]
    m = lines[1]
    end = len(lines)
    positions = []

    for i in lines[2:end]:
        positions.append(i)

    matrisLista = sdk.sudokuDFS(n, m, positions)
    return matrisLista
