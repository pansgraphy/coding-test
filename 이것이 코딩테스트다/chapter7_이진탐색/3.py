# 내가 풀었는데 이렇게 풀면 시간초과 때려먹는다... N의 범위 보는거 훈련하자!

# n, target = map(int, input().split())
# dduk = list(map(int, input().split()))

# h = 0
# while True:
#     sum_dduk = 0
#     h += 1 
#     for i in dduk:
#         x = i - h
#         if x < 0:
#             x= 0
#         sum_dduk += x

#     if sum_dduk <= target:
#         break

# print(h)

# -------------------------------------

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

