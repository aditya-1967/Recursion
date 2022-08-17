# Factorial of a number

def summation_parameter(i, total):
    if i < 1:
        print(total)
        return
    total *= i
    summation_parameter(i-1, total)

summation_parameter(5, 1)

# Fucntional Way

def summation_fucntional(n):
    if n < 1:
        return 1
    return n * summation_fucntional(n-1)

print(summation_fucntional(5))