from bisect import bisect_right, bisect_left

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards.sort()

def binary_search(array, target):
    a = bisect_left(array, target)
    b = bisect_right(array, target)
    return b - a
for target in nums:
    print(binary_search(cards, target), end=' ')