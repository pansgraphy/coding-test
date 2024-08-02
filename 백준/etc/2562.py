tmp = 0
index = 0
for i in range(9):
    num = int(input())
    if tmp < num:
        tmp = num
        index = i+1
print(tmp)
print(index)
