from heapq import heappush, heappop

MAX = 40000000

def solution(n, s, a, b, fares):
    adjL = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        adjL[c].append((d, f))
        adjL[d].append((c, f))
        
    d_from_s = dijkstra(s, adjL, n)
    d_from_a = dijkstra(a, adjL, n)
    d_from_b = dijkstra(b, adjL, n)
    
    answer = MAX
    for m in range(1, n + 1):
        answer = min(answer, d_from_s[m] + d_from_a[m] + d_from_b[m])
    return answer


def dijkstra(start, graph, n):
    dist = [MAX for _ in range(len(graph))]
    dist[start] = 0
    
    pq = []
    heappush(pq, (0, start))
    while pq:
        cost, v = heappop(pq)
        
        if dist[v] < cost:
            continue
        
        for w, v_to_w in graph[v]:
            via_cost = cost + v_to_w
            if via_cost < dist[w]:
                dist[w] = via_cost
                heappush(pq, (via_cost, w))
    return dist
                