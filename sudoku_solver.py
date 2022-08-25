# Sudoku Solver
# Leetcode 37

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]


def check(board, row, col, value):
    for i in range(9):
        if board[i][col] == str(value):
            return False
        if board[row][i] == str(value):
            return False
        if board[3 * (row // 3) +  (i // 3)][3 * (col // 3) + (i % 3)] == str(value):
            return False
    return True


def solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                for c in range(1, 10):
                    if check(board, i, j, c):
                        board[i][j] = str(c)
                    if solve(board):
                        return True
                    else:
                        board[i][j] = '.'
                return False
    return True

print(board)

solve(board)

print(board)