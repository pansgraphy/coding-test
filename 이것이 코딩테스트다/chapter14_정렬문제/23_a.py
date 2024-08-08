# 튜플의 특성을 이용 -> 각 튜플을 구성하는 원소의 순서에 맞게 정렬됨
# 리스트의 원소를 튜플로!
# [(),()]
# 뭐야 개꿀이잖아?!

n = int(input())
students = []

# 모든 학생의 정보 입력받기
for _ in range(n):
    students.append(input().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])

