# n, k = map(int, input().split())

# array = []

# for i in range(2):
#     array.append(list(map(int, input().split())))

# for i in range(k):
#     index_a = array[0].index(min(array[0]))
#     index_b = array[1].index(max(array[1]))

#     array[0][index_a], array[1][index_b] = array[1][index_b], array[0][index_a]

# result = 0
# for i in array[0]:
#     result += i

# print(result)

# ----------------------

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
