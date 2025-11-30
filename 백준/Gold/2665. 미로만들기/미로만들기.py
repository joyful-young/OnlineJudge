import sys
from heapq import heappop, heappush
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input())
arr = [input().strip() for _ in range(N)]
dist = [[N * N for _ in range(N)] for _ in range(N)]
dist[0][0] = 0

hq = []
heappush(hq, (0, 0, 0))
while hq:
    d, r, c = heappop(hq)

    if dist[r][c] < d:
        continue

    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            cost = d + 1 if arr[nr][nc] == "0" else d

            if cost < dist[nr][nc]:
                dist[nr][nc] = cost
                heappush(hq, (cost, nr, nc))

print(dist[N - 1][N - 1])