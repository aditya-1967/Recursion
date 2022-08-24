# N-Queens
# Leetcode 56

n = 4
col, posDiag, negDiag = set(), set(), set()
res = []

board = [['.'] * n for i in range(n)]

def backtrack(r):
    if r == n:
        temp = ["".join(row) for row in board]
        res.append(temp)
        return
    
    for c in range(n):
        if c in col or (r+c) in posDiag or (r-c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c] = 'Q'

        backtrack(r + 1)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = '.'

backtrack(0)
print(res)


