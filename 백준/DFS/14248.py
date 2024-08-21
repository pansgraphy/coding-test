from collections import deque

n = int(input())
node = list(map(int, input().split()))
s = int(input()) -1
visited = [False] * n

def bfs(start):
    q = deque([(node[start], start)])
    while q:
        ji = q.popleft()
        jump = ji[0]
        index = ji[1]
        for plus in range(1, jump + 1):
            di = plus + index
            if di < n and visited[di] == False:
                visited[di] = True
                q.append((node[di], di))

        for minus in range(index - jump, index):
            di = minus
            if di >= 0 and visited[di] == False:
                visited[di] = True
                q.append((node[di], di))

    print(visited.count(True))




bfs(s)

# 헷갈리는게.. 한번 점프를 쓰면 끝인 느낌인가..?
# 예시가 더 없으니까 헷갈림..
