# 00시 00분 00초
# 3이 하나라도 들어가있으면 카운팅
N = int(input())
cnt = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)