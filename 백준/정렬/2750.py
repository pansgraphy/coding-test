n = int(input())
data = []
result = []

for i in range(n):
    data.append(int(input()))
data.sort()

for i in data:
    print(i)