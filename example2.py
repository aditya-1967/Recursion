#Print Name n times

n = int(input('Enter n: '))

def print_name(i, n):
    if i == n:
        return 
    print('Winchester')
    print_name(i+1, n)

print_name(0, n)
