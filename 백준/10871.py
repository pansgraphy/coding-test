import sys

N, S = map(int, sys.stdin.readline().split())
nums = sys.stdin.readline().strip()
li = nums.split(' ')
numslist = list(map(int, li))
answer = ''

for i in numslist:
    if i < S:
        answer = answer + str(i)+ " "
print(answer)