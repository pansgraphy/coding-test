# 모든 간선의 비용이 1 => 너비 우선 탐색 (BFS)을 이용하여 최단 거리를 찾을 수 있다.
# 너비 우선 탐색 / 시간복잡도 O(N + M)

# 입력
# graph - 도로정보 받음(인덱스 = ~도시에서 / 값 = ~도시까지
# distance - 출발지로 부터 도착하는 도시까지의 최단거리

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색 (BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단거리가 k인 도시가 없다면, -1 출력
if check == False:
    print(-1)






# ------


# 모든 간선 길이 1 = BFS
# BFS의 시간복잡도는 O(노드 + 간선)
# BFS -> deque
# graph, distance, q

from collections import deque

# 입력
n, m, k, x = map(int, input().split())
# 거리정보 넣을 리스트 생성
graph = [[] for _ in range(n + 1)]

# 거리정보 입력받기 및 변수 넣기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리계산용 변수 생성
distance = [-1] * (n  + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.leftpop()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
