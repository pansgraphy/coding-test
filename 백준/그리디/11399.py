n = int(input())
times = list(map(int, input().split()))

times.sort()
answer = 0

for i in range(1, len(times)+1):
    for j in range(i):
        answer += times[j]

print(answer)

## 난 뭐이리 어렵게 생각했을까.. 굳이 2중 for문..
