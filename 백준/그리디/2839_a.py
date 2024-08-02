# https://puleugo.tistory.com/27
# 경우의 수를 나눠서 진행함
# 1. 가장 큰 단위인 5만으로 나눠 담는 것
# 2. 최소한의 3과 최대한의 5를 사용하여 나눠 담는 것
# 3. 3으로 나눠 담는 것
# 4. 나눠지지 않을 때

n = int(input())

if n % 5 == 0:  # 5으로 나눠떨어질 때
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif n == 0:  # 3으로 나눠떨어질 때
            print(p)
            break

# ------------------

N = int(input())
cnt = 0

while N >= 0:
    #5로 나누어 떨어질 때 break
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    
    #3kg 봉투 한 개씩 빼기
    N -= 3
    cnt += 1

#루프가 '자연적'으로 끝나는 경우 실행
else:
    print(-1)