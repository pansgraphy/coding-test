# 아이디어 : 큰 수부터 나눠서 몫 더하기
n, k = map(int, input().split())
money = []

for _ in range(n):
    data = int(input())
    if data <= k:
        money.append(data)

money.sort(reverse=True)

cnt = 0
i = 0
while k > 0:
    if money[i] <= k:
        cnt += k // money[i]
        k %= money[i]
    i += 1
    

print(cnt)
