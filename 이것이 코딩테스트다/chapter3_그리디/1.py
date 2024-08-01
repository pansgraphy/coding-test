# 큰 수의 법칙

N, M, K = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort(reverse=True)
a = K*(M//K)
print(numList[0]*a+numList[1]*(M-a))