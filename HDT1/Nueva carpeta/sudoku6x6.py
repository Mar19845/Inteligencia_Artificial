board = [[0,6,0,0,0,0], # This is the Sudoku Puzzle shown in a list/array.
        [0,0,0,6,2,4],
        [3,0,4,0,1,0],
        [0,0,0,2,0,0],
        [0,0,0,4,5,0],
        [0,0,1,0,0,2]]

def print_board(bo): # This is a utility function defined for printing the sudoku board/puzzle in the output.

    for m in range(len(bo)):
        if m % 2 == 0 and m != 0: # This will be the output printing the number of rows of the board.
            print("- - - - - - - - ") # Prints a horizontal line when in the second row.

        for c in range(len(bo[0])): # This will check all positions in the row is in the right column and eventually draw a vertical line.
            if c % 3 == 0 and c != 0: # This will be the number of squares separating from the other columns and drawing a vertical line between those two.
                print(" | ", end="") # Prints an output to make spaces between nums and making lines vertically.

            if c == 5: # Here we will check if we are the last position to make sure that backslash is there before going on to the next line.
                print(bo[m][c])
            else:
                print(str(bo[m][c]) + " ", end="") # This will print the board and writing it as a string function and printing it with spaces in between the numbers and then printing a new line.


def solution(bo): # Defining Function to solve the sudoku puzzle/board.
    find = find_empty_spaces(bo) # This will find the empty spaces where the zeros are.
    if not find: # If the statement for finding the empty spaces is not correct then it will return a boolean with True.
        return True
    else: # The Else statement would remove the digit and try another based on the find statement in all row and columns
        row, col = find

    for m in range(1,7): #Digits 1-6
        if valid(bo, m, (row, col)): # If all looks promising then it will make an attempt to solve.

            bo[row][col] = m # Making an attempt to solve.

            if solution(bo): # If the solution is a success it will return a boolean with True Statement.
                return True

            bo[row][col] = 0 # If it fails, it will try again and in doing so trigger the backtracking.


    return False # This triggers the backtracking algorithm


def valid(bo, num, pos):
    # Checking each row if its equal to the number entered.
    for m in range(len(bo[0])):
        if bo[pos[0]][m] == num and pos[1] != m: # If the number is in the position we just inserted, it will ignore it.
            return False

    # Checking each columns if its equal to the number inserted.
    for m in range(len(bo[1])):
        if bo[m][pos[1]] == num and pos[0] != m: # If the number is in the position we entered in the column , it will once again ignore it.
            return False

    # Check squares
    squares_x = pos[1] // 2   # Checks which position squares or boxes we are in the X value. This will give us value 0,1,2.
    squares_y = pos[0] // 3  # Checks which position squares or boxes we are in the Y value.

    # This will loop all elements in those squares/boxes and make sure that the same numbers wont appear twice.
    for m in range(squares_x *2,squares_x* 2): # Here we multiply the square that are from the X value with 3 to get to index 6.
        for c in range(squares_y *3, squares_y *3): # Same as above, we multiply squares from Y value with 3 to get to index 6.
            if bo[row][col] == num and (m,c) != pos:  # Checks if all elements in board are equal to the num added, and making sure it doesnt checks same position we added in and finally if that is true, it will return false because of duplicate numbers.
                return False
    return True  # If all these checks are fine, this will be a valid position in the board and return everything True and make it valid.

print("Welcome to my first Sudoku Puzzle!") # Prints a welcome greeting.
print("  ") # Prints a space between.
print("Original Output") # Prints a message indicating the Original Output.
print("  ") # Prints a space after the message above between the board and the message.

def find_empty_spaces(bo): # Defining function to find empty squares by 0.
    for m in range(len(bo)): # Finding the empty blanks in the columns of the board.
        for c in range(len(bo[0])): # Finding the empty spaces in the rows, in other words the 0 in the rows of the board.
            if bo[m][c] == 0: # Check if the position is 0.
                return (m,c)   # Returning the answer for all rows and columns.

    return False # If there is no squares that equals to 0 then it will trigger the find solution and make it true and say we are done.


print_board(board) # Prints the board itself with the original input.
print("__________________________") # Prints a horizontal line for visual separation purposes for the original and solved puzzle.
print("  ") # Prints a space between.
print("Solution with Backtracking Algorithm") # Prints a text above the solved puzzle.
print("  ") # Prints another space between.
solution(board) # Prints the finished solved board.
print_board(board) # Prints the board itself.
print("  ") # Prints space between.
print("Success!") # Prints a text saying Success! in the bottom end.