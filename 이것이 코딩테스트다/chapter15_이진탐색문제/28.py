n = int(input())
array = list(map(int, input().split()))
result = 0

def binarySect(array, start, end):
    mid = (start + end) // 2

    # 찾은경우
    if array[mid] == mid:
        return mid
    # 왼쪽
    elif array[mid] > mid:
        return binarySect(array, 0, mid - 1)
    # 오른쪽
    elif array[mid] < mid:
        return binarySect(array, mid + 1, end)

    # 없는경우
    if mid == start or mid == end:
        return -1

result = binarySect(array, 0, n - 1)
print(result)
