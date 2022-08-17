# Print n to 1 using backtracking

def print_backtracking(i, n):
    if i > n:
        return
    print_backtracking(i+1, n)
    print(i)

n = int(input('Enter number: '))
print_backtracking(1, n)