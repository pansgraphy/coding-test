data = list(input())
r = ord(data[0])
c = int(data[1])
dxdy = [[-2, 1], [-2, -1], [2, 1],[2, -1], [1, -2], [1, 2], [-1, -2], [-1, 2]]
cnt = 0
for i in dxdy:
    x = r + i[0]
    y = c + i[1]
    if x < 97 or y < 1:
        continue
    else:
        cnt += 1

print(cnt)
