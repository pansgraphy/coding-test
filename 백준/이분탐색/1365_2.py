n = int(input())
data = list(map(int, input().split()))
result = [data[0]]
def binary_search(array, target):
    start = 0
    end = len(array)
    mid = (start + end) // 2
    while start <= end:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1

    return mid

for i in range(1, len(data)):
    if data[i] > result[-1]:
        result.append(data[i])
    else:
        idx = binary_search(result, i)
        result[idx] = data[i]

print(len(data) - len(result))

