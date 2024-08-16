# dfs 인거 같은데.. 떠오르질 않는다... 외워야하나..
# 아니 서로소 집합 문제네이..

import sys
input = sys.stdin.readline

tour, city = map(int, input().split())
graph =[]

for i in range(tour):
    graph.append(list(map(int, input().split())))

print(graph)