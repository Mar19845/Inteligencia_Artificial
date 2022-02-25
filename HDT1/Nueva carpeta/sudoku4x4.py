###sudoku resolver 
M = int(input("que sudoku desea resolver"))
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(M):
        if grid[row][x] == num:
            return False
             
    for x in range(M):
        if grid[x][col] == num:
            return False
 
 
    if M == 4:
        val = 2
    elif M == 9:
        val = 3
    startRow = row - row % val
    startCol = col - col % val
    for i in range(2):
        for j in range(2):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''
grid = [[2, 0, 0, 4],
        [4, 0, 3, 0],
    [0, 2, 4, 1],
    [1, 4, 0, 3]]
   
 
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")