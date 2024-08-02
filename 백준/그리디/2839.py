# 출력 : 봉지 최소 샤용 개수
# 정확하게 n kg 못만들면 리턴 -1
# 봉지는 3kg, 5kg
# 아이디어 : 큰 봉지인 5kg 부터 담고 나머진 3kg 으로 담는다.

# 25분 풀었는데 모르겠음..

n = int(input())
count = 0

def aaaa(n, count):
    if n % 5 == 0:
        return n / 5
    
    count += (n // 5)
    n = n % 5
    count += (n // 3)
    n = n % 3
    if n != 0:
        return -1
    return count

result = aaaa(n, count)
print(result)