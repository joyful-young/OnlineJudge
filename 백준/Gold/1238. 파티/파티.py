import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, X = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
rev_adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    adjL[s].append((e, t))
    rev_adjL[e].append((s, t))


def dijkstra(start, graph):
    dist = [1000000] * (N + 1)
    visited = [False] * (N + 1)
    dist[start] = 0
    visited[start] = True

    hq = []
    heappush(hq, (0, start))
    while hq:
        cost, v = heappop(hq)

        if dist[v] < cost:
            continue

        for w, v_to_w in graph[v]:
            via_cost = cost + v_to_w
            if via_cost < dist[w]:
                dist[w] = via_cost
                heappush(hq, (via_cost, w))
    return dist

x_to_other = dijkstra(X, adjL)
other_to_x = dijkstra(X, rev_adjL)

print(max([x_to_other[i] + other_to_x[i] for i in range(1, N + 1)]))