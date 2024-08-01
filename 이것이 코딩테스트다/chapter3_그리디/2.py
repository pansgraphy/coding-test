N, M = map(int, input().split())
data = []
answer = 0
for i in range(N):
    d = list(map(int, input().split()))
    data.append(d)
    m = min(d)
    if m > answer:
        answer = m

print(answer)