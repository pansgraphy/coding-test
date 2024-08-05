# https://ggasoon2.tistory.com/38
import sys

n = int(input())

endPoint: int = 0
answer: int = 0

arr = []

for i in range(0,n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))

for newStart, newEnd in arr:
    if endPoint <= newStart:
        answer += 1
        endPoint = newEnd
print(answer)


# https://velog.io/@seungjae/%EB%B0%B1%EC%A4%80-1931%EB%B2%88-%ED%9A%8C%EC%9D%98%EC%8B%A4-%EB%B0%B0%EC%A0%95-Python-Greedy-Silver-1

# 1. 끝나는 시간 기준으로 정렬
# 2. 루프 돌면서 회의 시작시간이 기준이 되는 회의 끝나는 시간보다 크거나 같을때 채택


import sys
N = int(sys.stdin.readline())
timeline = []
for i in range(N):
    start, end = map(int,sys.stdin.readline().split())
    timeline.append((start, end))

timeline.sort(key=lambda x : (x[1],x[0]))
count = 1
end = timeline[0][1]
for i in range(1, N):
    if timeline[i][0]>=end:
        end = timeline[i][1]
        count += 1

print(count)