array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)



# 튜플일때, 두번째 값을 기준으로 정렬하기
array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result2 = sorted(array2, key=setting)
print(result2)

