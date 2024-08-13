n = int(input())
money = list(map(int, input().split()))
total_money = int(input())
money.sort()

# 상한액 정하기 -> mid 값으로 시작해서,
def binary_search(array, start, end):
    high = (start + end) // 2
    cal = 0
    for data in array:
        if data > high:
            cal += high
        else:
            cal += data

    if cal > total_money:
        return binary_search(array, start, high - 1)

    elif cal < total_money:
        return binary_search(array, high + 1, end)


binary_search(money, money[0], money[-1])