# dp 반복식
# 점화식 dp[row][col] = max(dp[row-1][col] ,dp[row-1][col-1] )
n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

dp = []
for i in range(1, n+1):
    dp.append([0 for _ in range(i)])
dp[0] = triangle[0]

for row in range(1, n):
    for col in range():



# result = 0
# for i in dp[n-1]:
#     result = max(result, i)
# print(result)

