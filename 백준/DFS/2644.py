import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [0] * (n + 1)

for i in range(m):
    p, c = map(int, input().strip().split())
    graph[c] = p

cnt = 0

def dfs(x):
    global cnt
    # 자식노드가 비었으면
    if graph[x] == 0:
        return x
    else:
        cnt += 1
        return dfs(graph[x])

a = dfs(a)
b = dfs(b)
if a == b:
    print(cnt)
else:
    print(-1)