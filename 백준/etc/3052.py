a = []
for _ in range(10):
    num = int(input())
    a.append(num%42)

print(len(list(set(a))))