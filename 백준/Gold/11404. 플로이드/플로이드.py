# 백준 11404. 플로이드
import sys
import heapq
input = sys.stdin.readline


def dijkstra(s):
    heap = []
    heapq.heappush(heap, (0, s))

    while heap:
        cost, v = heapq.heappop(heap)
        if cost > distance[v]:
            continue
        for c, b in adjL[v]:    # v에서 갈 수 있는 곳 b, 비용 c
            tmp = distance[v] + c
            if distance[b] > tmp:
                distance[b] = tmp
                heapq.heappush(heap, (tmp, b))

    for i in range(1, n + 1):
        if distance[i] == INF:
            distance[i] = 0
    print(*distance[1:])


n = int(input())
m = int(input())
adjL = [[] for _ in range(n + 1)]   # n개의 도시
for _ in range(m):
    a, b, c = map(int, input().split())     # 시작 도시, 도착 도시, 비용
    adjL[a].append([c, b])      # a와 버스 노선으로 연결된 도시 b, 비용 c

INF = 1e8
for i in range(1, n + 1):
    distance = [INF for _ in range(n + 1)]
    distance[i] = 0     # 출발점 거리 0
    dijkstra(i)