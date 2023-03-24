# 백준 1753. 최단경로
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())    # 정점 개수, 간선 개수
K = int(input())    # 시작 정점
graph = [[] for _ in range(V + 1)]      # 정점 번호는 1부터 V까지
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))     # u와 연결된 정점 v. 가중치는 w

INF = 1e9
min_distance = [INF for _ in range(V + 1)]  # 각 정점에 대해 시작점으로부터의 최단거리 초기화
min_distance[K] = 0

heap = []
heapq.heappush(heap, (0, K))    # 시작점에서 시작점으로 가는 거리, 시작점 번호
while heap:
    to_now, now = heapq.heappop(heap)     # 현재 위치의 시작점으로부터의 거리, 현재 위치
    if to_now > min_distance[now]:      # 먼저 구해 놓은 거리가 더 작으면 이미 방문했던 곳
        continue
    for dist, node in graph[now]:       # 현재 위치에서 갈 수 있는 곳
        tmp = dist + to_now         # 현재 위치를 거쳐서 node까지 가는 거리
        if tmp < min_distance[node]:    # 먼저 구해 놓은 최단거리보다 tmp가 더 작으면 갱신
            min_distance[node] = tmp
            heapq.heappush(heap, (tmp, node))


for i in range(1, V + 1):
    if min_distance[i] == INF:
        print('INF')
    else:
        print(min_distance[i])
