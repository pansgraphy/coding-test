# 아이디어 :
# B 배열의 원소 크기가 큰 수에 각각 차례대로 A 배열의 작은수를 매칭 해주면 될 것 같음
# 헷갈리는 것 : B는 아예 건드리면 안됨? 그럼 b값을 복사한 다른걸로 해도 되는건가.. 이런게 헷갈림
import sys

# 입력받기
n = int(sys.stdin.readline().strip())
a = list(map(int, input().split()))
b = list(map(int, sys.stdin.readline().strip()))

# a 값을 오름차순으로 정렬
a.sort()

# b의 큰값에 따른 정보 수집

# (값, 인덱스) 튜플 리스트 생성
indexed_array = [(value, index) for index, value in enumerate(b)]
# 값에 따라 내림차순 정렬
sorted_indexed_array = sorted(indexed_array, key=lambda x: x[0], reverse=True)

# 이럴 빠에 그냥 보는게 나을듯..!


