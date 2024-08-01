N, M = map(int, input().split())
x, y, direction = map(int, input().split())
dot_map = []

for i in range(N):
    data = list(map(int, input().split()))
    dot_map.append(data)

dxdy = [[0, -1], [-1, 0], [0, 1], [1, 0]]

cnt = 1
sea = 0
while True:
    if sea == 4:
        break
    direction += 1
    cur_x = x + dxdy[(direction+4)%4][0]
    cur_y = y + dxdy[(direction+4)%4][1]
    if dot_map[cur_x][cur_y] == 0:
        x = cur_x
        y = cur_y
        dot_map[cur_x][cur_y] = 1
        cnt += 1
        sea = 0
    else:
        sea += 1
print(cnt)

## 좀 더 다듬을 필요가 있음,, 디테일 부족함