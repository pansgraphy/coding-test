# 뭐야.. 나 엄청 복잡하게 했잖아...

# https://velog.io/@keynene/Python-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-7568-%EB%8D%A9%EC%B9%98

import sys

tc = int(sys.stdin.readline().strip())
person = []

#2차원 배열로 입력값 저장
for _ in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    person.append([a,b]) 
    #[[a1,b1], [a2,b2] ...]

for size in person: #비교대상 : person[0](55,185)
    rank = 1
    for comp in person: #비교할대상 : person[0~4](55,185 ~ 46,155)
        if size[0] < comp[0] and size[1] < comp[1]:
            rank += 1
    print(rank, end=' ')

# 자기자신과 나머지를 모두 비교하면서 자기자신이 비교대상보다 키, 몸무게 다 작으면 rank + 1
# 그리고 출력, 다시 rank 초기화 하고 다시 비교,, tc번 반복
