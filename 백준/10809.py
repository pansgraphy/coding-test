import string
alist = list(string.ascii_lowercase)
answer = [-1 for _ in range(26)]

s = list(input())

for i, e in enumerate(s):
    index = alist.index(e)
    if answer[index] == -1:
        answer[index] = i
    
print(' '.join(map(str, answer)))