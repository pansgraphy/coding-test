# 모든 경우의 수를 구하고 k에 맞게 출력?
# 애초에 k를 이용해 풀기?
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

graph = []
# 자신의 위치 (r, 0)
# 집의 위치 (0, c)

def dfs():
    d = [(0,1),(0,-1),(1,0),(-1,0)]

    