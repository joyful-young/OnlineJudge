# 백준 2252. 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]      # 진입차수
for _ in range(M):
    A, B = map(int, input().split())
    # A가 B의 앞이어야 함
    adjL[A].append(B)
    degree[B] += 1      # B의 진입차수 +1

queue = deque()

for i in range(1, N + 1):
    if degree[i] == 0:      # 진입차수가 0인 것 큐에 넣기
        queue.append(i)

ans = []

while queue:
    t = queue.popleft()     # 큐에서 꺼내서
    ans.append(t)           # 답에 넣고

    for v in adjL[t]:       # t 정점에 인접한 v
        degree[v] -= 1      # 진입차수 -1

        if degree[v] == 0:      # 진입차수가 0이 되었으면
            queue.append(v)

print(*ans)
