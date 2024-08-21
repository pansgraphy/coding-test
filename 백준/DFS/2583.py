import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
cnt = []
cnti = -1
# 자료 입력받아서 그래프에 사각형 넣기
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

def dfs(a, b, cnt, cnti):
    d = [(0, 1),(0, -1),(1, 0),(-1, 0)]
    graph[a][b] = 1
    for x, y in d:
        dx = x + a
        dy = y + b

        if 0 <= dx < m and 0 <= dy < n and graph[dx][dy] == 0:
            graph[dx][dy] = 1
            cnt[cnti] += 1
            dfs(dx, dy, cnt, cnti)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnti += 1
            cnt.append(1)
            dfs(i, j, cnt, cnti)
cnt.sort()
print(len(cnt))
print(*cnt, sep=' ')
