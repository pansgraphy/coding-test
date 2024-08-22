import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [n] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x ,graph):
    global visited
    visited[x] -= 1

    for i in graph[x]:
        dfs(graph[i], graph)

dfs(1, graph)

print(*visited, sep=' ')