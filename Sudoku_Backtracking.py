import time

board =  [[0,3,4,0,0,0,6,0,0],                 
         [0,0,2,6,0,0,0,8,0],
         [0,6,8,3,0,0,0,0,7],
         [0,0,3,0,0,1,0,0,5],
         [0,5,9,0,6,0,0,7,2],
         [0,0,0,5,2,0,0,4,6],
         [2,0,5,9,0,6,0,0,0],
         [0,0,0,4,0,8,0,5,0],
         [0,0,0,0,0,7,0,0,4]]

def valid_steps(row, col, num):
    for i in range(0,9):
        if board[row][i] == num:
            return False

    for i in range(0,9):
        if board[i][col] == num:
            return False
    
    local_square_row = (row // 3) * 3
    local_square_col = (col // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if board[local_square_row+i][local_square_col+j] == num: 
                return False

    return True

def sudoku_solution():
    for row in range(0,9):
        for col in range(0,9):
            if board[row][col] == 0:
                for num in range(1,10): 
                    if valid_steps(row, col, num):
                        board[row][col] = num # will exhaust my recursion tries without this line 
                        sudoku_solution()
                        board[row][col] = 0

                return

    for row in range(0,9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(0,9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


start_time = time.time()
sudoku_solution()
end_time = time.time()

print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()
print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()
print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()
print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()
print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()
print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()
print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()
print("Time taken to solve Sudoku: {:.2f} seconds".format(end_time - start_time))
sudoku_solution()








    
            

