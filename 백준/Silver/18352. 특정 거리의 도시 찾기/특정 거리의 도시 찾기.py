# 백준 18352. 특정 거리의 도시 찾기 - 시간초과

import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

adjL = [[] for _ in range(N + 1)]   # 0번 비우고 1번부터 N번

for _ in range(M):
    A, B = map(int, input().split())
    adjL[A].append(B)       # 단방향 도로

# print(adjL)

min_d = [1000000 for _ in range(N + 1)]
min_d[X] = 0    # X번 도시에서 X번 도시로 가는 최단거리는 0

visited = [False for _ in range(N + 1)]

heap = []
heapq.heappush(heap, (min_d[X], X))     # 최소 힙에 (그 도시까지 최단경로, 도시번호) 넣기

while heap:       # 다음에 방문할 도시가 없어서 heap이 빌 때까지
    # print(heap)
    t = heapq.heappop(heap)
    # print(adjL[t[1]])
    for city in adjL[t[1]]:    # t와 인접한 도시 중
        if not visited[city] and t[0] + 1 < min_d[city]:   # 방문 안 한 도시이고 이전에 계산한 거리보다 t를 거쳐 가는 거리가 더 작으면
            min_d[city] = t[0] + 1
            heapq.heappush(heap, (min_d[city], city))

    visited[t[1]] = True       # t 방문 처리

# print(visited)
# print(min_d)
flag = False
for city in range(1, N + 1):
    if min_d[city] == K:     # 최단거리가 K인 도시
        flag = True
        print(city)     # 출력

if not flag:    # 최단거리 K인 도시가 없어서 flag가 False이면
    print(-1)
