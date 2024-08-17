from collections import deque
import sys

input = sys.stdin.readline
k = int(input())

q = deque()

for i in range(k):
    num = int(input())
    if num == 0:
        q.pop()
    else:
        q.append(num)

print(sum(result))