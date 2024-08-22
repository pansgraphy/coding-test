import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j, graph):
    d = [(0,1),(0,-1),(1,0),(-1,-0),(-1,-1),(-1,1),(1,1),(1,-1)]

    if graph[i][j] == 0:
        return
    else:
        graph[i][j] = 0
        for x, y in d:
            dx = x + i
            dy = y + j
            if 0 <= dx < h and 0 <= dy < w:
                dfs(dx, dy, graph)

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().rstrip().split())))

    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j, graph)
    print(cnt)
