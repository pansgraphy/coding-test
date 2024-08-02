# 출력 : 통일시는 최소 횟수
# 어떻게 해야 최소 횟수가 나올까?
# 카운트 방식 : 연속된 수를 뒤집을때마다 +1
# 0과 1의 연속됨을 카운트 해서 적은것을 출력! 

# 어떻게 연속이 꺠진것을 확인하지?
# i-1이 i랑 같은지 비교?

s = input()
zero_cnt = 0
one_cnt = 0

if s[0] == '1':
    zero_cnt += 1
else:
    one_cnt += 1

check = int(s[0])

for i in range(1, len(s)):
    if check != int(i) and (check * 1) == 0:
        zero_cnt += 1
    elif check != int(i) and (check * 1) == 1:
        one_cnt += 1
    else:
        continue

print(min(zero_cnt, one_cnt))

