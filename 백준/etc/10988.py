s = list(input())
a = int(len(s)/2)
answer = 1
for i in range(a):
    if s[i] != s[len(s)-1-i]:
        answer = 0
print(answer)
