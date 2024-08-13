# 2750이랑 같은 문제인데
# 시간복잡도 문제인듯?
# 그렇담 힙정렬? ->> 똑같이 시간초과

import sys
import heapq

n = int(input())
heap = []

for i in range(n):
    heapq.heappush(heap, sys.stdin.readline().rstrip())

for i in heap:
    print(heapq.heappop(heap))