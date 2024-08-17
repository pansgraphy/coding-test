import sys

x = int(sys.stdin.readline().rstrip())

cnt = 1
row = 1
col = 1

# False 일때 왼쪽 밑으로
# True 일때, 오른쪽 위로
flag = False

while cnt < x:
    
    if row == 1 and flag == False:
        col += 1
        flag = True
    elif col == 1 and flag == True:
        row += 1
        flag = False
    # 왼쪽 밑으로 대각선
    elif flag == True:
        row += 1
        col -= 1
    # 오른쪽 위로 대각선
    elif flag == False:
        row -= 1
        col += 1

    cnt += 1


fraction = str(row) + '/' +str(col)
print(fraction)

# 시간을
# 줄이려면...
# 어떻게..
#  