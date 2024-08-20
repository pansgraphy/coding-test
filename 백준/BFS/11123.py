#  몇 개의 양무리가 있었는지 출력

from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(x, y):
    global d, h, w, graph
    graph[x][y] = '.'
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == '#':
                graph[nx][ny] = '.'
                q.append((nx, ny))


for tc in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    
    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                bfs(i, j)
                cnt += 1
    
    print(cnt)




# 정답 이후 참고
# https://jinho-study.tistory.com/910
# dfs로도 가능
