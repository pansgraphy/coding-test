# s를 알 때, 서로 다른 n의 개수가 최대
# == 작은 수 부터 빼가면서 카운트 하기?
# 근데 떨어져야함 == 합이 S 가 되어야함

# 3 -> 1 2
# 4 -> 1 3
# 5 -> 1 4
# 6 -> 1 2 3
# 7 -> 1 2 4
# 8 -> 1 3 4
# 9 -> 2 3 4
# 10 -> 1 2 3 4 // 4
# 11 -> 1 3 7 // 3

s = int(input())
