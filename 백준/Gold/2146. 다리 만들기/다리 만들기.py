# 2146. 다리 만들기

import sys
from collections import deque
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float('inf')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def label_islands_and_get_edges(si, sj, label):
    q = deque([(si, sj)])
    arr[si][sj] = label
    edges = []
    while q:
        xi, xj = q.popleft()
        is_edge = False
        for di, dj in DIR:
            ni, nj = xi + di, xj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = label
                    q.append((ni, nj))
                else:
                    is_edge = True
        if is_edge:
            edges.append((xi, xj))
    return edges


def get_shortest_bridge(edges):
    start_island_label = arr[edges[0][0]][edges[0][1]]
    q = deque(edges)
    visited = [[INF for _ in range(N)] for _ in range(N)]
    for si, sj in edges:
        visited[si][sj] = 0

    while q:
        xi, xj = q.popleft()

        for di, dj in DIR:
            ni, nj = xi + di, xj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == INF and arr[ni][nj] != start_island_label:
                if arr[ni][nj] == 0:
                    visited[ni][nj] = visited[xi][xj] + 1
                    q.append((ni, nj))
                else:
                    return visited[xi][xj]
    return None

# 섬 구분, 섬 가장자리 저장
island_number = 2
island_edges_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            island_edges_list.append(label_islands_and_get_edges(i, j, island_number))
            island_number += 1

results = []
# 섬 가장자리-다른 섬 최단 거리 구하기
for island_edges in island_edges_list:
    bridge = get_shortest_bridge(island_edges)
    if bridge is not None:
        results.append(bridge)

print(min(results))
