# 빈 공간 '.'(점)
# 울타리를 '#'
# 늑대를 'v'
# 양을 'k'

# 단, 울타리로 막히지 않은 영역에는 양과 늑대가 없으며 양과 늑대는 대각선으로 이동할 수 없다.
# 살아남게 되는 양과 늑대의 수를 각각 순서대로 출력한다.
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(map(int, input().split())))

