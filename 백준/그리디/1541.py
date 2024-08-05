# 아이디어: 
# 숫자와 부호 분리?
# - 뒤에 나오는 +는 다 -로 바꾸기
# eval() 사용?

n = input()
length = len(n)
cnt = 1
toggle = False
result = ''
for i in range(length):
    if n[i] == '-' and toggle == False:
        result = n[:i+cnt] + '(' + n[i+cnt:]
        toggle = True
        cnt += 1
    elif n[i] == '-' and toggle == True:
        result = n[:i+cnt] + ')' + n[i+cnt:]
        toggle = False
        cnt += 1
    elif i == (length-1) and toggle == True:
        result += ')'

if result == '':
    print(eval(n))
else:
    print(eval(result))


# 아.. 0 제거 해야하네..
# 50분 정도 고민해봤는데 0은 너무 오래걸릴거 같음
# 답을 본다..