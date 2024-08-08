# # 자료구조 뭘 선택해야함??..
# 일단 집들의 위치가 주어졌을때,
# 1 부터 가장 수가 큰 집까지 탐색하면서
# 케이스를 모두 검색하면 되려나? -> BFS?

# 너무 많을 것 같으니,, 길이를 반으로 나눠서
# 집이 많은쪽으로 + 혹은 - 시키면서 찾는게 맞지 않을까?

# 아니 이거 정답률 왜이래.. 다 나같은 사람들인가?


n = int(input())
data = list(map(int, input().split()))
result = 0
def dfs(data):
    global result






    return min(result, x)

