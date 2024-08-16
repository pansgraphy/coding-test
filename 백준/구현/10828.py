from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
stack = deque()
v = -1

for i in range(n):
    commend = input().split()
    # push 일때, 명령어와 정수 분리
    if commend[0] == 'push':
        stack.append(commend[1])
        v += 1
    # pop 일때,
    elif commend[0] == 'pop':
        if v < 0:
            print(-1)
        else:
            tmp = stack.pop()
            print(tmp)
            v -= 1
    # size 일때,
    elif commend[0] == 'size':
        print(len(stack))
    # empty 일때,
    elif commend[0] == 'empty':
        if v < 0:
            print(1)
        else:
            print(0)
    # top 일때,
    else:
        if v < 0:
            print(-1)
        else:
            print(stack[v])
