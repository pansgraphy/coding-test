import copy

num = int(input())
array = map(int, input().split())
b = copy.deepcopy(array)
a = max(array)

result = 0
i = 0
for e in (b):
    result += e/a*100
    i += 1

print(result/i)