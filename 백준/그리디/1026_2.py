# a만 재배치 = b에 맞게 a를 재배치

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n

a.sort()
rank = []

for i in range(n):
    rank.append((b[i], i))

rank.sort(reverse=True)

for i in range(n):
    c[rank[i][1]] = a[i]

result = 0
for i in range(n):
    result += c[i] * b[i]

print(result)