# 아 문제를 이해 못하겠다..

n = int(input())

lope = []
for i in range(n):
    lope.append(int(input()))

lope.sort()

print(n*lope[0])