n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards.sort()

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return print(0, end =' ')
    if array[mid] == target:
        return print(1, end =' ')
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] <= target:
        return binary_search(array, target, mid + 1, end)

for target in nums:
    binary_search(cards, target, 0, n - 1)


