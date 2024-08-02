s = input()
result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if result == 0:
        result += num
    elif num != 1 and num != 0:
        result *= num
    else:
        result += num

print(result)