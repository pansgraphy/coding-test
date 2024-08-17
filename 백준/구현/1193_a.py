# https://velog.io/@hwsa1004/%EB%B0%B1%EC%A4%80-1193%EB%B2%88-%EB%B6%84%EC%88%98%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4

# 몇번째 줄 몇번째 원소인지 알아낸다
# while num > line:
#     num -= line
#     line += 1

# 이런 규칙성은 어찌 찾아내냐...

# 좀더 자세한 설명
# https://blognavercomcheetah254.tistory.com/38

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')
            