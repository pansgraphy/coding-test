# https://velog.io/@jw2957/%EB%B0%B1%EC%A4%80-10815%EB%B2%88-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import bisect
N = int(input())
card = list(map(int, input().split()))
M = int(input())
other = list(map(int, input().split()))
card.sort()
answer = [0] * M
for o in other:
    l = bisect.bisect_left(card, o)
    r = bisect.bisect_right(card, o)
    print(r - l, end=' ')


# --------
# https://juni-tech.tistory.com/25

import sys

def binary_search(array, check, start, end):
  if start > end:
    return False
  mid = (start + end) // 2
  if check == array[mid]:
    return True
  elif check > array[mid]:
    start = mid + 1
    return binary_search(array, check, start, end)
  else:
    end = mid - 1
    return binary_search(array, check, start, end)

input = sys.stdin.readline

N = int(input())
your_card = sorted(list(map(int, input().rstrip().split())))

M = int(input())
compare_card = list(map(int, input().rstrip().split()))

for num in compare_card:
  if binary_search(your_card, num, 0, N-1):
    print(1, end=' ')
  else:
    print(0, end=' ')