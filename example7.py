# Sum of first n numbers

# Parameterised Way

def summation_parameter(i, total):
    if i < 1:
        print(total)
        return
    total += i
    summation_parameter(i-1, total)

summation_parameter(5, 0)

# Fucntional Way

def summation_fucntional(n):
    if n < 1:
        return 0
    return n + summation_fucntional(n-1)

print(summation_fucntional(5))