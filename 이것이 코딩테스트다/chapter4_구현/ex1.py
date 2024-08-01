N = int(input())
data = list(map(str, input().split()))
xy = [1, 1]
for i in range(len(data)):
    if data[i] == 'L':
        xy[1] -= 1
        if 0 in xy:
            xy[1] += 1
    elif data[i] == 'R':
        xy[1] += 1
        if 0 in xy:
            xy[1] -= 1
    elif data[i] == 'U':
        xy[0] -= 1
        if 0 in xy:
            xy[0] += 1
    else:
        xy[0] += 1
        if 0 in xy:
            xy[0] -= 1

print(xy)
