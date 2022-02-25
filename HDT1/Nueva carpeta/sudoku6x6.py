

def print_board(bo): 

    for m in range(len(bo)):
        for c in range(len(bo[0])): 

            if c == 5:  
                print(bo[m][c])
            else:
                print(str(bo[m][c]) + " ", end="") 


def solution(bo):
    find = find_empty_spaces(bo) 
    if not find: 
        return True
    else: 
        row, col = find

    for m in range(1,7): 
        if valid(bo, m, (row, col)): 

            bo[row][col] = m 

            if solution(bo): 
                return True

            bo[row][col] = 0


    return False 


def valid(bo, num, pos):
    for m in range(len(bo[0])):
        if bo[pos[0]][m] == num and pos[1] != m: 
            return False

    for m in range(len(bo[1])):
        if bo[m][pos[1]] == num and pos[0] != m: 
            return False

    squares_x = pos[1] // 2  
    squares_y = pos[0] // 3  


    for m in range(squares_x *2,squares_x* 2):
        for c in range(squares_y *3, squares_y *3):
            if bo[row][col] == num and (m,c) != pos:  
                return False
    return True  


print("Original Output")
print("  ") 

def find_empty_spaces(bo): 
    for m in range(len(bo)): 
        for c in range(len(bo[0])): 
            if bo[m][c] == 0: 
                return (m,c)  

    return False 

