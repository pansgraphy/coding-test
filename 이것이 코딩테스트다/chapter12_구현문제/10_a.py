# 자물쇠와 열쇠의 크기는 20 x 20 보다 작다. 20 x 20 = 400
# python 1초 = 2000만 ~ 1억
# 해결 아이디어 = 완전탐색
# 수월하게 하기 위해서 자물쇠 리스트의 크기를 3배 이상으로 변경하고 가운데에 3 x 3 위치한다.
# 홈이 맞는지 계산은 0 + 1 = 1 이니까 1이 되면 홈이 맞는 것이다.
# 즉 모든 값이 1이면 되는 것!

# 여기선 matrix_by_90_degree() 함수 구현함 -> 90도 회전
# 2차원 배열 다둘때 가끔 사용되므로 노트에 적어두길!


# https://school.programmers.co.kr/learn/courses/30/lessons/60059

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solutions(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

