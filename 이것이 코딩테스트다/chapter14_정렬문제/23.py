
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

# 출력 : 정렬한 이름

n = int(input())
data = []
for i in range(n):
    name, ko, en, ma = map(str, input().split())
    data.append([name, int(ko), int(en), int(ma)])

# 1. 국어 점수가 감소하는 순서로
data.sort(reverse = True, key = lambda x:x[1])

# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
tmp = []
for i in range(n-1):
    if data[i][1] == data[i+1][1]:
        if data[i][2] > data[i+1][2]:
            
    else:
        tmp.append(data[i])




for i in range(n):
    print(data[i])







