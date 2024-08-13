import sys

n = int(sys.stdin.readline().rstrip())
datas = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    datas.append([x, y])

datas.sort(key = lambda x: (x[0], x[1]))

for data in datas:
    print(data[0], data[1])

# 348ms

# ------
# 다른사람들 풀이는 거의
# 요런느낌?

n = int(input())
li = []

for i in range(n):
    a, b = map(int, input().split())
    li.append([a,b])
li.sort()

for a, b in li:
    print(a, b)

# 2728ms

## 내가 푼게 매우 빠르니.. 이렇게 하는걸로..!