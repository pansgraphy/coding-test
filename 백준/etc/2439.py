import sys

n = int(sys.stdin.readline())

for i in range(n):
    n -= 1
    print(' '*n+'*'*(i+1))