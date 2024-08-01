n = int(input())

data = []

for i in range(n):
    num = int(input())
    data.append(num)

result = sorted(data, reverse=True)

for i in result:
    print(i, end=' ')