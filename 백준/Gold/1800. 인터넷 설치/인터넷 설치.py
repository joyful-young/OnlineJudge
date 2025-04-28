import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(max_cost):
    hq = []
    heappush(hq, (0, 1))
    
    dist = [K + 1 for _ in range(N + 1)]
    dist[1] = 0

    while hq:
        cost, v = heappop(hq)
        if dist[v] < cost:
            continue

        for w, v_to_w in adjL[v]:
            via_cost = cost + 1 if v_to_w > max_cost else cost
            if via_cost < dist[w]:
                dist[w] = via_cost
                heappush(hq, (via_cost, w))
    return dist[N] <= K

N, P, K = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
for _ in range(P):
    a, b, c = map(int, input().split())
    adjL[a].append((b, c))
    adjL[b].append((a, c))

left = 0
right = 1000000
answer = -1
while left <= right:
    mid = (left + right) // 2

    if dijkstra(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
