stNum = list(range(1,31))
# print(stNum)
for _ in range(28):
    number = int(input())
    stNum.remove(number)

for e in stNum:
    print(e)
