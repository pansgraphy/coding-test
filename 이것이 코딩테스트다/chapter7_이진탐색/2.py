import time
start_time = time.time()

n = int(input())
n_data = list(map(int, input().split()))
n_data.sort()
m = int(input())
m_data = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in range(m):
    print(binary_search(n_data, m_data[i], 0, n - 1), end=" ")


end_time = time.time()
print()
print('-----------------------------')
print("time :", end_time - start_time)