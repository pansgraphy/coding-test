n = int(input())
i = 0
cnt = 0
while True:
    if n > i: # n이 i보다 크면 n에 i를 차감
        i += 1
        n = n-i
        cnt += 1
    else:
        print(cnt)
        break

# 출처: https://lazypazy.tistory.com/59 [Redddy's Devlog:티스토리]

# 1부터 +1 해서 더하다가
# 남은 값을 더해버리는 것..?

# -------------
# https://velog.io/@boyfromthewell/%EB%B0%B1%EC%A4%80-1789%EB%B2%88-%EC%88%98%EB%93%A4%EC%9D%98-%ED%95%A9-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# n까지 1부터 더해가다가 n보다 큰값이 나오면, 그 직전의 수가 문제의 정답

n=int(input())
sum=0
result=0
for i in range(1, n+1):
  sum+=i
  result+=1
  if sum>n:
    result-=1
    break
    
print(result)