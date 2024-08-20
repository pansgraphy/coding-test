# 1. 중복제거
# 2. 0과 1 각각 카운트
# 3. 더 작은 갯수 출력?
# 예외 -> 1개의 숫자만 있다면(둘 중 하나라도 0이면) 0출력

import sys
input = sys.stdin.readline

s = input().rstrip()
check = [0, 0]
check[int(s[0])] += 1
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        check[int(s[i])] += 1

if check[0] == 0 or check[1] == 0:
    print(0)

else:
    print(min(check))