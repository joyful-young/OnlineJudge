# 백준 1504. 특정한 최단 경로

import sys
import heapq
input = sys.stdin.readline


def dijkstra(s, g):
    # v1 != N, v2 != 1 조건은 있는데 v1이 1이 아니고 v2가 N이 아니라는 조건 없음
    if s == g:          # 이거 없으면 어딘가를 거쳐서 다시 돌아오는 게 최단경로로 잡힘
        return 0
    q = []
    heapq.heappush(q, [0, s])
    min_distance = [INF] * (N + 1)
    while q:
        dist, now = heapq.heappop(q)

        if min_distance[now] < dist:
            continue
        for c, b in adjL[now]:
            tmp = dist + c
            if tmp < min_distance[b]:
                min_distance[b] = tmp
                heapq.heappush(q, (tmp, b))
    return min_distance[g]


N, E = map(int, input().split())
adjL = [[] for _ in range(N + 1)]   # 1번 ~ N번 정점
for _ in range(E):
    a, b, c = map(int, input().split())
    adjL[a].append([c, b])      # a에서 갈 수 있는 정점 b, 거리는 c
    adjL[b].append([c, a])      # 양방향

v1, v2 = map(int, input().split())  # 반드시 거쳐야 하는 두 개의 정점

INF = 10 ** 9
# 반드시 어떤 정점을 거쳐서?
# 1 -> v1 -> v2 -> N
d1 = dijkstra(1, v1)
d2 = dijkstra(v1, v2)
d3 = dijkstra(v2, N)
# print(d1, d2, d3)

if d1 != INF and d2 != INF and d3 != INF:
    tmp1 = d1 + d2 + d3
else:
    tmp1 = INF
# print(tmp1)

# 1 -> v2 -> v1 -> N
d1 = dijkstra(1, v2)
d2 = dijkstra(v2, v1)
d3 = dijkstra(v1, N)
# print(d1, d2, d3)

if d1 != INF and d2 != INF and d3 != INF:
    tmp2 = d1 + d2 + d3
else:
    tmp2 = INF
# print(tmp2)

ans = min(tmp1, tmp2)
if ans != INF:
    print(ans)
else:
    print(-1)