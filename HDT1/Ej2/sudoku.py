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
        print(x,y,c)
        
    