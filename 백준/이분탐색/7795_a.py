# https://velog.io/@a87380/7795%EB%B2%88-%EB%A8%B9%EC%9D%84-%EA%B2%83%EC%9D%B8%EA%B0%80-%EB%A8%B9%ED%9E%90-%EA%B2%83%EC%9D%B8%EA%B0%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 오잉 뭐가 다르길래 이사람은 시간초과가 아닌겨..
# 아 다르네ㅎㅎ 흠..


T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort()

    start = 0
    count = 0
 
    for j in range(N):
        while True:

            if start==M or A[j]<=B[start]:
                count+=start
                break
            else:   
                start+=1
                
    print(count)

################

import bisect

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (bisect.bisect(B, a-1))
    print(cnt)

# 라이브러리 완전 까먹고 있었음...
# https://jinho-study.tistory.com/311

def binary_search(li, a):
    s, e = 0, len(li)-1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if li[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res
    
    
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (binary_search(B, a) + 1)
    print(cnt)