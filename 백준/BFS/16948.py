# 최소를 구해야하네...
# min()??

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

graph = [[-1] * (n) for _ in range(n)]
# [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
graph[r1][r1] = 0


def bfs(r1, c1):
    # cnt = 0
    # check = False
    q = deque()
    q.append((r1, c1))

    while q:
        r, c = q.popleft()
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            
            if graph[nr][nc] == -1:
                graph[nr][nc] = graph[r][c] + 1 # 방문체크
                q.append((nr, nc))


bfs(r1, c1)
print(graph[r2][c2])