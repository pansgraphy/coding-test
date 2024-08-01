import sys
import copy

n = int(sys.stdin.readline())
nlist = map(int, sys.stdin.readline().split())
blist = copy.deepcopy(nlist)
print(str(min(nlist))+" "+str(max(blist)))