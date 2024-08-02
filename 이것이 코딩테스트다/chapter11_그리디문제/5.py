# 두 사람이 고를 수 있는 볼링공의 번호의 조합!
# 경우의 수
# n = 공의 개수
# m = 공의 최대 무게

from itertools import combinations

n, m = map(int, input().split())
weight = list(map(int, input().split()))
s_weight = set(weight)
cal = len(weight) - len(s_weight)
print(len(list(combinations(weight, 2))) - cal)

# 조합에 볼링공중에 중복되는 무게 공 갯수 만큼 빼기