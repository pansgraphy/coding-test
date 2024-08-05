import sys
S = sys.stdin.readline().strip().split('-') # - 기준으로 괄호를 치면 최소로 만들 수 있음
temp = []
for i in S: # 각 요소에 대해
    cnt = 0
    for j in i.split('+'): # +로 짼 요소들을
        cnt += int(j) # 더하고
    temp.append(cnt) # 모아주자
# 모아준 temp들을 맨 앞 인덱스 제외하고 전부 빼면 최소값
result = temp[0]
for i in temp[1:]:
    result -= i
print(result)
# 출처: https://edder773.tistory.com/242 [개발하는 차리의 학습 일기:티스토리]

# 1. +와 -로 이루어진 숫자 계산식에 괄호를 쳐서 최솟값을 만들려 한다는 건 즉 - 사이의 숫자들을 모두 더해서 빼주면 된다는 뜻이다.예를 들어 25-20+15-5+10+15 이런 숫자가 있다면 최소로 만들어주려면 25 - (20 + 15) - (5 + 10 + 15)로 만들어서 계산하면 -40으로 최소를 얻을 수 있다.
# 2. split을 통해 먼저 -를 기준으로 나누어주고, 나누어진 리스트를 더해주기 위해서 각각 + 로 나누고, 각 값들을 더해준 요소들을 리스트에 모아준다.
# 3. -를 기준으로 빼줘야 하니 리스트 맨 앞의 숫자에서부터 나머지 숫자들을 빼나 가면 최솟값을 구할 수 있다.
# 출처: https://edder773.tistory.com/242 [개발하는 차리의 학습 일기:티스토리]


# -----------

exp = input().split('-') #'-'를 기준으로 split해서 exp 리스트에 저장

num = [] #'-'로 나눈 항들의 합을 저장할 리스트

for i in exp:
    sum = 0
    tmp = i.split('+') #덧셈을 하기 위해서 '+'를 기준으로 split
    for j in tmp: #split한 리스트의 각 요소들을 더해줌
        sum += int(j)
    num.append(sum) #각 항의 연산 결과(덧셈)를 num에 저장

n = num[0] #식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다

for i in range(1,len(num)): #1번째 값부터 n에서 빼준다
    n -= num[i]
print(n)

# https://sodehdt-ldkt.tistory.com/49
