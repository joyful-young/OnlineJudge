import sys
from heapq import heappush, heappop
input = sys.stdin.readline


N, M = map(int, input().split())
adjL = [[] for _ in range(N + 1)]

# in_degree[i]: i번 노드 진입차수. i번 문제를 풀기 전에 풀어야 할 문제 수
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)
    in_degree[b] += 1

hq = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heappush(hq, i)

answer = []
while hq:
    # 풀 수 있는 문제 중 가장 작은 것부터
    v = heappop(hq)
    answer.append(v)

    for w in adjL[v]:
        in_degree[w] -= 1
        if in_degree[w] == 0:
            heappush(hq, w)

print(*answer)