import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
adjL = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adjL[a].append((b, c))
    adjL[b].append((a, c))

def prim():
    hq = []
    heappush(hq, (0, 1))
    visited = [0 for _ in range(V + 1)]

    total = 0
    
    while hq:
        cost, v = heappop(hq)
        if visited[v] == 1:
            continue

        visited[v] = 1
        total += cost
        
        for w, v_to_w in adjL[v]:
            if visited[w] == 0:
                heappush(hq, (v_to_w, w))
    return total

print(prim())