def fac(n):
    if n == 0:
        return print(1)
    
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)


n = int(input())
fac(n)