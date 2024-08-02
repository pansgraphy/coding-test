dic = {
    2:['A', 'B', 'C'],
    3:['D', 'E', 'F'],
    4:['G', 'H', 'I'],
    5:['J', 'K', 'L'],
    6:['M', 'N', 'O'],
    7:['P', 'Q', 'R', 'S'],
    8:['T', 'U', 'V'],
    9:['W', 'X', 'Y', 'Z']
}

s = list(input())
answer = 0
for e in s:
    for key, values in dic.items():
        if e in values:
            answer += key

print(answer+(len(s)))