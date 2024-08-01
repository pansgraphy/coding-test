N, M = map(int, input().split())
bucket = []
for i in range(N):
    bucket.append(i+1)

for i in range(M):
    i, j = map(int, input().split())
    tmp = bucket[j-1]
    bucket[j-1] = bucket[i-1]
    bucket[i-1] = tmp

print(' '.join(map(str, bucket)))