# 모험가 길드
import queue

# n = int(input())
# x = list(map(int, input().split()))
n = 5
x = [2, 3, 1, 2, 2]

x.sort(reverse= True)
q = queue.Queue()
result = 0

for i in x:
    q.put(i)

data = q.get()

while q:
    if data > q.qsize()+1:
        break
    else:
        for _ in range(data-1):
            q.get()
        result += 1
        if q.qsize() < 0:
            break
        data = q.get()
    

print(result)


