a = [1, 1, 2, 2, 2, 8]
s = list(map(int, input().split()))
answer = [0 for _ in range(6)]

for i in range(len(a)):
    answer[i] = a[i] - s[i]

print(' '.join(map(str, answer)))