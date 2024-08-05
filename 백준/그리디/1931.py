# 회의 시작순으로 정렬하고,
# 같은 회의 시작시간일때, 회의가 짧은 것을 채택
# 종료 조건 : 리스트가 끝나면 그때까지 카운트 했던 것을 출력

n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append([start, end])

data.sort()
print(data)


# 막히는 점
# 1. 자료를 어떻게 보관하는게 효율적일까?
# 2. 알고리즘 자체가 떠오르지 않는다. -> 최대한의 회의개수를 필터링 하려면... 시간 순으로 적은 시간의 회의를 추려내면 될 것 같았는데
#    그렇지가 않음
# 3. 이거 dp 임?


