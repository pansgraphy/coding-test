from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())

edge = [[] for _ in range(n+1)]
visited = []

for i in range(m):
    a, b = map(int, input().split())
    edge.append((a, b))

def bfs(a, b, start):
    q = deque()
    q.append((a, b))

    while q:
        e = q.popleft()

