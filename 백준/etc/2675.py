N = int(input())

for _ in range(N):
    x = ''
    num, cha = input().split()
    for e in cha:
        x += e*int(num)
    print(x)