# nth Fibonacci number

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(12))
print(fibo(5))