# Sudoku Solver using Backtracking Algorithm

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)  # row, col
    return None
def is_valid(board, num, pos):
    # Check row
    for col in range(len(board[0])):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # Check column
    for row in range(len(board)):
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    # Check 3x3 box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solution found
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Reset if no solution forward

    return False

# Sample Sudoku board (0 represents empty spaces)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Initial Board:")
print_board(board)
solve(board)
print("\nSolved Board:")
print_board(board)
