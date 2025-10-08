import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = 1_000_000_000 + 1
N, M = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adjL[a].append((b, c))
    adjL[b].append((a, c))
    
S, E = map(int, input().split())


def dijkstra(s, e):
    hq = [(-INF, s)]
    limits = [0] * (N + 1)
    limits[s] = INF

    while hq:
        weight_limit, v = heappop(hq)

        if limits[v] > -weight_limit:
            continue

        for w, c in adjL[v]:
            # v를 거쳐서 w까지 갈 때의 중량제한
            tmp = min(c, -weight_limit)
            if tmp > limits[w]:
                limits[w] = tmp
                heappush(hq, (-tmp, w))
    return limits[e]

print(dijkstra(S, E))