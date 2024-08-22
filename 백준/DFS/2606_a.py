# 좀 더 심플하게 표현한 코드
# https://www.acmicpc.net/source/82831958

N = int(input())
M = int(input())
visited=[0]*(N+1)
net = [[] for i in range(N+1)]


for i in range(M):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

def dfs(v):
    visited[v] = True

    for i in net[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(sum(visited)-1)

# 다른 설명글 
# https://bio-info.tistory.com/152

