import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = -1
def dfs(graph, i):
    global cnt
    if visited[i] == 0:
        visited[i] = 1
        cnt += 1
        for i in graph[i]:
            dfs(graph, i)

    return cnt


print(dfs(graph, 1))