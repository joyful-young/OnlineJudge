import sys
from heapq import heappush, heappop
input = sys.stdin.readline

MAX_D = 2000 * 1000
def dijkstra(start, graph, nodes):
    dist = [MAX_D for _ in range(nodes + 1)]
    dist[start] = 0
    
    hq = []
    heappush(hq, (0, start))
    while hq:
        c, v = heappop(hq)

        if dist[v] < c:
            continue

        for w, v_to_w in graph[v]:
            s_v_w = dist[v] + v_to_w
            if s_v_w < dist[w]:
                dist[w] = s_v_w
                heappush(hq, (s_v_w, w))
    return dist

    
T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adjL = [[] for _ in range(n + 1)]
    g_to_h = MAX_D
    for _ in range(m):
        a, b, d = map(int, input().split())
        adjL[a].append((b, d))
        adjL[b].append((a, d))
        if {a, b} == {g, h}:
            g_to_h = d

    from_s = dijkstra(s, adjL, n)
    from_h = dijkstra(h, adjL, n)
    from_g = dijkstra(g, adjL, n)

    candidates = [int(input()) for _ in range(t)]
    ans = []
    for e in candidates:
        s_g_h_e = from_s[g] + g_to_h + from_h[e]
        s_h_g_e = from_s[h] + g_to_h + from_g[e]
        
        if from_s[e] == min(s_g_h_e, s_h_g_e):
            ans.append(e)
    ans.sort()
    print(*ans)