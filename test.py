lock = [[1,1,1], [1,1,0], [1,0,1]]
# b = [[1,2], [1,2], [1,3]]

for i in range(len(lock)):
    for j in range(len(lock[i])):
        if lock[i][j] == 1:
            lock[i][j] = 0
        else:
            lock[i][j] = 1

print(lock)

