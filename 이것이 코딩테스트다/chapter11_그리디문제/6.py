def solution(food_times, k):
    target = 0
    length = len(food_times)
    
    while k > 1:
        for i in range(length):
            if food_times[i] > 0:
                food_times[i] -= 1
            k -= 1
            target = i+1
    if target == length:
        return 1
    else:
        return target
    


# https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3

# 30분 안에 풀기 실패
# 테스트 케이스 몇개만 성공
# 시간 초과.. 역시 이런 문제는 시간복잡도 이용해야 하는 듯..
