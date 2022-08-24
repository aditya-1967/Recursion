# N Queens II
# Leetcode 52

n = 4
col, posDiag, negDiag = set(), set(), set()
res = 0

def backtrack(r):
    if r == n:
        global res
        res += 1
        return
    
    for c in range(n):
        if c in col or (r+c) in posDiag or (r-c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)

        backtrack(r + 1)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)

backtrack(0)
print(res)


