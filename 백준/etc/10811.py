N, M = map(int, input().split())
array = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    array[i-1:j] = array[i-1:j][::-1]

print(' '.join(map(str, array)))