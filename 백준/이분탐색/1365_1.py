import bisect

n = int(input())
data = list(map(int, input().split()))

result = [data[0]]

for i in range(1, len(data)):
    if data[i] > result[-1]:
        result.append(data[i])
    else:
        idx = bisect.bisect_left(result, data[i])
        result[idx] = data[i]

print(len(data)-len(result))