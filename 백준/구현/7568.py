import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    x, y = map(int, input().split())
    data.append((x, y, i))

data.sort(reverse=True)

rank = []
#rank 초기값 설정
rank.append((data[0][2], 1))
r = 1
cp = 0
for i in range(1, n):
    # 다음 순위 일때
    if data[i-1][0] > data[i][0] and data[i-1][1] > data[i][1]:
        r += 1
        rank.append((data[i][2], r+cp))
        cp = 0
    # 같은 등수 일때
    elif data[i-1][0] >= data[i][0] and data[i-1][1] <= data[i][1]:
        rank.append((data[i][2], r))
        cp += 1

rank.sort()
for i in range(n):
    print(rank[i][1], end = ' ')