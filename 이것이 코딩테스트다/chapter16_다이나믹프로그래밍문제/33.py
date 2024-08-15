# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# 출력 = 최대이익

n = int(input())
tp = []
tp.append(0)
for i in range(n):
    t, p = map(int, input().split())
    tp.append((t, p))

result = 0
for i in range(1, n+1):
    #초기값
    t, p = tp[i]
    price = 0
    
    while i <= n:
        t, p = tp[i]
        if i == n and t != 1:
            break
        price += p
        i += t
    
    result = max(result, price)

print(result)


## 문제점 -> 알고리즘 설계를 좀 잘못함. 건너뛰어야 하는 경우를 놓침(일부러 안하는 케이스)

