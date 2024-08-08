import heapq

result = 0
heap = []
cnt = 0

n = int(input())
for i in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) > 0:    
    if cnt == 2:
        result *= 2
        cnt = 0
    a = heapq.heappop(heap)
    result += a

    cnt += 1

print(result)

## 출력초과뜸...