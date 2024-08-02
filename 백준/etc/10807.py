import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
t = sys.stdin.readline()
li = s.split(' ')
b = list(map(int, li))
print(b.count(int(t)))