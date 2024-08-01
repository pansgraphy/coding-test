N, M = map(int, input().split())
bucket = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    bucket[i-1:j] = [k] * ((j) - (i-1))

print(' '.join(map(str, bucket)))
