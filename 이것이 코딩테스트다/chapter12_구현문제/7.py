# 아이디어
# 입력은 짝수로만 들어온다.
# 1. 입력을 반으로 쪼갠다
# 2. 반복문으로 원소를 더한다.
# 3. 더한 값을 비교하고 출력한다.

n = input()
s = len(n) // 2
a = n[:s]
b = n[s:]

left = 0
right = 0

for i in range(s):
    left += int(a[i])
    right += int(b[i])

if left == right:
    print("LUCKY")
else:
    print("READY")