# N, M = map(int, input().split())

# graph = []
# for i in range(N):
#     graph.append(list(map(int, input())))

# result = 1
# x = 0
# y = 0

# graph[0][0] = 0

# while True:

#     if graph[x+1][y] == 1:
#         x += 1
#         graph[x][y] = 0
#     elif graph[x][y+1] == 1:
#         y += 1
#         graph[x][y] = 0
#     elif graph[x][y-1] == 1:
#         y -= 1
#         graph[x][y] = 0
#     elif graph[x-1][y] == 1:
#         x -= 1
#         graph[x][y] = 0

#     result += 1

#     if x == N-1 and y == M-1:
#         break

# print(result)


from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][nx] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))


