# coding-test

# dp

## 가장 긴 증가하는 부분 수열

```
n = int(input())
array = list(map(int, input().split()))

array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))
```

    •	BFS: 가중치가 동일한 그래프에서 최단 경로를 구할 때 유용.
    •	DFS: 최단 경로보다는 특정 조건을 만족하는 경로를 탐색할 때 유용.
    •	다익스트라: 양수 가중치를 가진 그래프에서 하나의 시작점에서 다른 모든 정점으로의 최단 경로를 구할 때 사용.
    •	플로이드-워셜: 모든 정점 쌍 간의 최단 경로를 구해야 할 때, 특히 음수 가중치가 있는 경우 사용.
