
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로


n = int(input())
data = []
for i in range(n):
    s = input()
    if s not in data:
        data.append(s)

data.sort(key= lambda x : (len(x), x))

for i in data:
    print(i)

# ------------

import sys

n = int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s not in data:
        data.append(s)

data.sort(key= lambda x : (len(x), x))

for i in data:
    print(i)