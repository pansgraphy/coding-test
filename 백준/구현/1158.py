import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = [0 for i in range(n)]
v = -1

for i in range(n):
    cnt = 0
    while cnt < k:
        v += 1
        if data[v%n] == 0:
            cnt += 1
    data[v%n] = 1
    print("<"v%n+1)
