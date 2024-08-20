from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = 0
y = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            x = i
            y = j

def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'X':
                continue

            if graph[nx][ny] == 'O':
                graph[nx][ny] = 'V'
                q.append((nx, ny))
            if graph[nx][ny] == 'P':
                graph[nx][ny] = 'V'
                q.append((nx, ny))
                cnt += 1

            # 벽으로 막혀져있는곳에 사람이 있으면 예외해야하는디..
    return cnt

result = bfs(x, y)
if result == 0:
    print('TT')
else:
    print(result)
