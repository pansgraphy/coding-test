t = int(input())
a = 300
b = 60
c = 10

check = True
cnt = [0, 0, 0]
if t % c != 0:
    check = False

else:
    if t >= a:
        cnt[0] = t // a
        t %= a
    if t >= b:
        cnt[1] = t // b
        t %= b
    if t >= c:
        cnt[2] = t // c
        t %= c
    
    if t != 0:
        check = False

if check:
    for i in cnt:
        print(i, end=' ')
else:
    print(-1)

