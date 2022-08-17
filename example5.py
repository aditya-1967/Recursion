# Print 1 to n using Backtracking

def print_backtracking(i, n):
    if i < 1:
        return
    print_backtracking(i-1, n)
    print(i)

n = int(input('Enter a number: '))
print_backtracking(5, n)
