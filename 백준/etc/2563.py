N = int(input())
A = []
for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.append(tmp[0]+10)
    tmp.append(tmp[1]+10)
    A.append(tmp)

for i in range(N-1):
    for j in range(N-1):
