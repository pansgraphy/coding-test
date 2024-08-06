# https://school.programmers.co.kr/learn/courses/30/lessons/60059
# 어렵군..
# key 는 M x M
# lock은 N x N
# M은 항상 N 이하

# 1. 90도 회전
# 2. 상.하.좌.우 이동 (0으로 채움)


def solution(key, lock):
    answer = True
    
    return answer


lock = [[1,1,1], [1,1,0], [1,0,1]]

for i in range(len(lock)):
    for j in range(len(lock[i])):
        if lock[i][j] == 1:
            lock[i][j] = 0
        else:
            lock[i][j] = 1

print(lock)