# https://yeoooo.github.io/algorithm/BOJ14248/

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
v = [0]*(n+1)
bridge = list(map(int, input().split()))
s = int(input().rstrip())
cnt = 1
def dfs(x):
    global cnt
    for i in range(2):
        if not i:
            nx = x+bridge[x]
        else:
            nx = x-bridge[x]
        if 0<=nx<n and not v[nx]:
            v[nx] = 1
            cnt += 1
            dfs(nx)
dfs(s-1)
print(cnt)