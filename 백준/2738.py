# N, M = map(int, input().split())

# total = [[0 for _ in range(N)] for _ in range(M)]

# for i in range(N*2):
#     temp = list(map(int, input().split()))
#     for j in range(M*2):
#         total[i%N][j%M] += temp[j%M]/2

# for i in range(N):
#     a = map(int, total[i])
#     print(' '.join(map(str, a)))

# 계속 런타임에러뜸...
# 걍 참고해서 단순하게 해봄

A, B = [], []
N, M = map(int, input().split())
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=" ")
    print()