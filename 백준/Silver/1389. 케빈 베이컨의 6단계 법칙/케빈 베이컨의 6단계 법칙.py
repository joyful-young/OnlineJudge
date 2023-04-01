# 백준 1389. 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    q = deque()
    visited = [-1 for _ in range(N + 1)]    # 시작점을 0으로 할 거라 -1로 초기화
    q.append(s)     # 시작점 큐에 넣기
    visited[s] = 0

    while q:
        t = q.popleft()
        for n in adjL[t]:   # t에 인접한 노드들
            if visited[n] == -1:    # 방문하지 않은 노드이면
                q.append(n)     # 큐에 넣고
                visited[n] = visited[t] + 1     # 방문 표시(거리표시)
    return sum(visited[1:])     # 1번 인덱스부터 끝까지의 합 = 케빈 베이컨의 수


N, M = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

# print(adjL)

minV = 10000

for i in range(1, N + 1):
    tmp = bfs(i)
    if minV > tmp:          # 여러 명일 경우 번호 가장 작은 사람 -> 등호 없어야.
        minV = tmp
        ans = i             # 케빈 베이컨의 수 가장 작은 사람 찾기

print(ans)