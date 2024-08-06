# 대문자와 숫자의 분리
# 정렬, 합계산
# 출력

s = input()

c = []
num = 0
for i in s:
    if i <= 'Z' and i >= 'A':
        c.append(i)
    else:
        num += int(i)

c.sort()

result = ''
for i in c:
    result += i

print(result+str(num))