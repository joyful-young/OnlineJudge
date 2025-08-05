import sys
from heapq import heappush, heappop
input = sys.stdin.readline


N, M = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    adjL[a].append((b, t))
    adjL[b].append((a, t))

INF = float('inf')
def dijkstra(block=None):
    prev_city = [0] * (N + 1)    # 이전에 방문한 도시
    dist = [INF] * (N + 1)
    dist[1] = 0
    hq = [(0, 1)]

    while hq:
        d, v = heappop(hq)

        if dist[v] < d:
            continue

        for w, v_to_w in adjL[v]:
            if block is not None and \
            ((block[0] == v and block[1] == w) or (block[0] == w and block[1] == v)):
                continue

            start_to_w = d + v_to_w
            if start_to_w < dist[w]:
                dist[w] = start_to_w
                prev_city[w] = v
                heappush(hq, (start_to_w, w))
                
    return dist[N], prev_city

# 검문 안 할 경우 최단시간
normal_min_time, prev = dijkstra()

# 최단시간 경로 구하기
path = []
curr = N
while prev[curr] != 0:
    path.append((curr, prev[curr]))
    curr = prev[curr]

# 최단경로 내 도로 중 하나를 막았을 경우의 최단시간들 중 최댓값
blocked_max_time = 0
for a, b in path:
    min_time, _ = dijkstra((a, b))
    blocked_max_time = max(min_time, blocked_max_time)

if blocked_max_time == INF:
    print(-1)
else:
    print(blocked_max_time - normal_min_time)