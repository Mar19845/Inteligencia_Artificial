def sudokuDFS(n, m, positions):
    n = int(n)
    sudoku = []
    
    for i in range(0,n):
        row = []
        for j in range(0,n):
            row.append(0)
        
        sudoku.append(row)
    
    end = len(positions)

    for i in range(0, end):
        x, y, c = positions[i].split()
        x = int(x)
        y = int(y)
        c = int(c)
            
        sudoku[x-1][y-1]=c

    endSdk = len(sudoku)
    for i in range(0,endSdk):
        print(sudoku[i])





    