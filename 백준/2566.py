m = 0
r = 0
c = 0

for row in range(9):
    input_row = list(map(int, input().split()))
    if max(input_row) >= m:
        m = max(input_row)
        r = row+1
        c = input_row.index(m)+1

print(m)
print(r, c)

# 계속 틀렸는데 이유는 최대값이 0일때가 고려되지 않은 코드여서 그랬다.
# 그래서 7번줄에 > 를 >=로 고치니 통과되었다.