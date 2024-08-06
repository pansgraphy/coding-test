
s = 'abcdef'

result = []

for i in range(1, len(s)):
    tmp = []
    length = len(s)
    for j in range(0, len(s), i):
        tmp.append(s[j:j+i])

    for x in range(len(tmp)-1):
        if x[i] == x[i+1]:
            length -= i
    

print(min(result))