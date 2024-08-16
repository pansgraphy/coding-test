num = int(input())
cycle = 0
new = num
while True:
    left = new // 10
    right = new % 10

    tmp = (left + right) % 10
    new = right*10 + tmp
    
    cycle += 1

    if new == num:
        break

print(cycle)