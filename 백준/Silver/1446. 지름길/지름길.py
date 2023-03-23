# 백준 1446. 지름길 - 맨 마지막에 인덱스에러?!!!!

import sys
import heapq
input = sys.stdin.readline

N, D = map(int, input().split())    # 지름길 개수, 고속도로 길이
# 0에서 D까지의 최단거리 구해야 함
adjL = [[] for _ in range(D + 1)]   # 0에서 D까지

for i in range(D):
    adjL[i].append((i + 1, 1))      # 바로 다음으로 가는 거

for _ in range(N):
    start, end, length = map(int, input().split())
    if start <= D and end <= D:
        adjL[start].append((end, length))   # start에 연결되어있는 end와 그 길이

# print(adjL)

visited = [False for _ in range(D + 1)]
distance = [10000 for _ in range(D + 1)]
distance[0] = 0
heap = []
heapq.heappush(heap, (0, 0))   # 그 지점까지 최단거리, 지점 번호

while heap:
    now = heapq.heappop(heap)   # 현재 위치까지 최단거리, 현재 위치 번호

    for next, length in adjL[now[1]]:    # 현재 위치에 연결되어 있는 지름길
        if not visited[next] and distance[next] > now[0] + length:    # 방문 안했고 현재 위치 거쳐 가는 거리가 더 작으면
            distance[next] = now[0] + length
            heapq.heappush(heap, (distance[next], next))

    visited[now[1]] = True

# print(distance)
print(distance[D])