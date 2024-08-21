from collections import deque
import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
r, c = map(int, input().split())
result = -1
def bfs(r, c):
    global result
    q = deque([(r, c)])
    d = [(1, 0), (-1, 0), (0, 1),(0, -1)]
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0 or graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                
                if graph[nx][ny] == 1:
                    result = visited[nx][ny]
                    return result

bfs(r, c)
if result == -1:
    print(-1)
else:
    print(result)
