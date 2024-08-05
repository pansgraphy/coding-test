n = int(input())

rm = []
coins = [25, 10, 5, 1]

for i in range(n):
    rm.append(int(input()))

for rmv in rm:
    data = []
    for coin in coins:
        if rmv >= coin:
            data.append(rmv // coin)
            rmv %= coin
        else:
            data.append(0)
    
    for i in data:
        print(i, end=' ')
    print()

# 너무 간단한걸 복잡하게 짰네..ㅠ


