# 테스트케이스 부족으로 이해갸 좀 어려웠다.
# 적절히 로프를 선택해서 최대한 많이 들 수 있게끔 해야함
n = int(input())
k = []
for _ in range(n):
    k.append(int(input()))
k.sort()

answers = []
for x in k:
    answers.append(x*n)
    n -= 1
print(max(answers))

# https://puleugo.tistory.com/30

