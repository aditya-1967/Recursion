# Print Linearly from 1 to n

n = int(input('Enter n: '))

def print_linearly(i, n):
    if i > n:
        return
    print(i)
    print_linearly(i+1, n)

print_linearly(1, n)
    