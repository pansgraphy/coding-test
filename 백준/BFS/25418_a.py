# https://monogatary.tistory.com/98
# 크게 2가지 방법으로 풀 수 있을 것 같다.

# 1. BFS를 적용한 풀이 (이와 유사하게 동적 프로그래밍으로도 풀 수 있음)
# 현재 노드가 c 이면 c와 인접한 노드는 c+1, 2*c 라는 식으로 접근할 수 있다.
# 효율성을 위해 인접 노드가 목표 노드보다 값이 클 경우는 큐에 추가하지 않는다.
# 후술할 풀이보다 시간이 많이 걸린다.

# 2. 다른 풀이
# 위의 풀이와는 반대로 목표값에서 시작한다. 
# 2로 나눈 값이 시작값보다 작지 않은 동안, 2로 나눌 수 있다면 2로 나누고 나눌 수 없다면 1을 뺀다.
# 2로 나눈 값이 시작값보다 작다면, 연산을 중단하고 현재값과 시작값의 차 만큼을 횟수에 더하면 된다.


from collections import deque
a,k=map(int,input().split())
q=deque([a])
v={a:0}
while q:
    c=q.popleft()
    if c==k: break
    for x in [2*c,c+1]:
        if x in v or x>k: continue
        v[x]=v[c]+1
        q+=[x]
print(v[k])