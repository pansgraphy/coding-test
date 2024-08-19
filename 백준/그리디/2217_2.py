n = int(input())
data = []
for i in range(n):
    rope = int(input())
    data.append(rope)

print(min(data) * n)
