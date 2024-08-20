# 이어진 것을 어떻게 제대로 카운팅할지 모르겠네..

from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
# 글자인 부분 1이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결되어 있다면
move = [(0,1), (0,-1), (1,0), (-1,0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 and ny < 0 and nx >= n and ny >= m:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

            if graph[x][y] == 0 and graph[nx][ny] == 1:
                cnt += 1 

    return cnt


print(bfs(0, 0))