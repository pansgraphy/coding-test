# https://dmaolon00.tistory.com/entry/BOJPython-1439%EB%B2%88-%EB%92%A4%EC%A7%91%EA%B8%B0-%EA%B7%B8%EB%A6%AC%EB%94%94-%EB%AC%B8%EC%9E%90%EC%97%B4
# 내가 하려했던걸 좀더 간결하게 표현한 느낌

s = input()
zero = 0
one = 0

# 첫 숫자를 기준으로 묶음 개수 1로 설정
if s[0] == '0':
    zero += 1
else:
    one += 1

for i in range(len(s) - 1): # 주어진 문자열 탐색 시작
    if s[i] != s[i + 1]:    # 현재 숫자와 다음 숫자가 동일하지 않다면, 묶음 종료
        if s[i + 1] == '0': # 다음 숫자가 0이라면, 0의 묶음 개수를
            zero += 1
        else:               # 그렇지 않다면, 1의 묶음 개수를 1 증가
            one += 1

print(min(zero, one))       # 0과 1의 각 묶음 개수 중 작은 묶음의 개수가 최종 결과
