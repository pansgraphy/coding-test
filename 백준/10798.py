A = []
answer = ''
M = 0
for i in range(5):
    row = list(input())
    A.append(row)
    if len(row) > M:
        M = len(row)

for row in range(M):
    for col in range(5):
        try:
            answer += A[col][row]
        except:
            pass

print(answer)