# 1916. 최소비용 구하기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
M = int(input())

adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    adjL[s].append([e, c])

S, E = map(int, input().split())

dist = [10 ** 8 for _ in range(N + 1)]      # 시작점에서 각 노드까지의 비용


def dijkstra(start):
    pq = []
    heappush(pq, [0, start])
    dist[start] = 0

    while pq:
        cost, v = heappop(pq)

        if dist[v] < cost:
            continue

        for w, v_to_w in adjL[v]:
            via_cost = dist[v] + v_to_w
            if via_cost < dist[w]:
                dist[w] = via_cost
                heappush(pq, [via_cost, w])


dijkstra(S)
print(dist[E])