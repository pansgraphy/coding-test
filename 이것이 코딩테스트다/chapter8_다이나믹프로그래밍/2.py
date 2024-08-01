# 1 <= x <= 30,000
# 캐싱사용?

x = int(input())

cnt = 0

while True:
    minus1 = x - 1
    if minus1 % 5 == 0:
        x -= 1
        x //= 5
        cnt += 2
    elif x % 5 == 0:
        x //= 5
        cnt += 1
    elif minus1 % 3 == 0:
        x -= 1
        x //= 5
        cnt += 2
    elif x % 3 == 0:
        x //= 3
    elif minus1 % 2 == 0:
        x -= 1
        x //= 2
        cnt += 2
    elif x % 2 == 0:
        x //= 2

    if x == 1:
        break

print(cnt)