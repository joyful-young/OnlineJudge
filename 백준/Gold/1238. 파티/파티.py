import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, X = map(int, input().split())
MAX_DIST = 100000

adjL = [[] for _ in range(N + 1)]
rev_adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    adjL[s].append((e, t))
    rev_adjL[e].append((s, t))

def dijkstra(start, graph):
    dist = [MAX_DIST for _ in range(N + 1)]
    dist[start] = 0
    
    q = []
    heappush(q, (0, start))
    while q:
        # 출발점에서의 거리가 가장 짧은 노드
        cost, v = heappop(q)

        if dist[v] < cost:
            continue

        for w, v_to_w in graph[v]:
            via_cost = cost + v_to_w
            if via_cost < dist[w]:
                dist[w] = via_cost
                heappush(q, (via_cost, w))

    return dist

# X에서 각 마을로
x_to_other = dijkstra(X, adjL)

# 각 마을에서 X로. 역방향 그래프에서 X로부터의 최단거리 구함.
other_to_x = dijkstra(X, rev_adjL)

print(max([x_to_other[i] + other_to_x[i] for i in range(1, N + 1)]))
