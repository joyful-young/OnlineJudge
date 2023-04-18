# 백준 13549. 숨바꼭질 3
from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)
visited = [0] * 100001
visited[N] = 1
while q:
    t = q.popleft()
    if t == K:
        break

    if t * 2 <= 100000 and not visited[t * 2]:
        q.append(t * 2)
        visited[t * 2] = visited[t]

    for n in [t - 1, t + 1]:
        if 0 <= n <= 100000 and not visited[n]:
            q.append(n)
            visited[n] = visited[t] + 1

print(visited[K] - 1)   # 출발지점을 1로 설정해서 1 빼줘야 함.