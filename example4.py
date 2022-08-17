# Print n to 1

def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n-1)

n = int(input("Enter n: "))
print_reverse(n)