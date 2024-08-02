total = int(input())
num = int(input())
answer = 0

for _ in range(num):
    p, a = input().split()
    p = int(p)
    a = int(a)
    answer += p*a

if answer == total:
    print('Yes')
else:
    print('No')