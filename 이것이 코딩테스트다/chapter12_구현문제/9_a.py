# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solutions(s):
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동이하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

# 일단 접근법이 잘못된 듯 나는 스텝을 문자열 길이만금 가져가려고 했으나
# 어차피 길이가 문자열의 전체 길이의 반 이상이 되어버리면 의미 없는 것 같음
# 그래서 step을 전체길이 // 2 로 가져가는 부분..

# min을 처리하는 방법도 모든 케이스를 다 담아서 min을 추출하는게 아닌
# 스텝별로 for 문이 끝날때, 비교해가며 솎아냄

