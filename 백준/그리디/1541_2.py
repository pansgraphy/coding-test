s = input()

lencnt = 0 # 정수의 자릿수

for c in s:
    if c != '+' and c != '-':
        lencnt += 1
    else:
        break

toogle = False
result = int(s[0:lencnt])
for i in range(lencnt, len(s) - lencnt, lencnt+1):

    if c == '-' and toogle == False:
        toogle = True
        result -= int(s[i+1:i+lencnt+1])
    elif toogle == True:
        result -= int(s[i+1:i+lencnt+1])
    elif c == '+' and toogle == True:
        result += int(s[i+1:i+lencnt+1])
    else:
        result += int(s[i+1:i+lencnt+1])



print(result)


