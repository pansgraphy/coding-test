n = int(input())
b = n-1
a = 2

for i in range(1, n*2):
    if i <= n:
        print(' '*b + '*'*(i*2-1))
        b -= 1
    else:
        print(' '*(i-n) + '*'*((n*2-1)-a))
        a += 2
