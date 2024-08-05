p = int(input())

rm = 1000 - p
coins = [500, 100, 50, 10, 5, 1]
result = 0
for i in coins:
    if rm >= i:
        result += rm // i
        rm %= i
        

print(result)