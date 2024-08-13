import sys

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))
c = set(n_list)
for i in m_list:
    if i in c:
        print(1)
    else:
        print(0)

# 152ms

## 원래는 이진탐색을 요하는 문제였던 것 같기도?
# https://iamzieun.tistory.com/12

import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for m in M_list:
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if m > N_list[mid]:
            left = mid + 1
        elif m < N_list[mid]:
            right = mid - 1
        else:
            left = mid
            right = mid
            break
            
    if left == mid and right == mid:
        print(1)
    else:
        print(0)

# 616ms


# 이진탐색이 시간이 . 더걸리네...
# 유형에 따라 다른가보다..!