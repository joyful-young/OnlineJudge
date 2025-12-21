import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline


INF = float('inf')
dr = [-1, 0, 1, 0]    # 상우하좌
dc = [0, 1, 0, -1]
N = int(input())
house = [input().rstrip() for _ in range(N)]

# 문 위치 확인
start = None
end = None
for i in range(N):
    for j in range(N):
        if house[i][j] == "#":
            if start is None:
                start = (i, j)
            else:
                end = (i, j)


def can_pass(r, c):
    return 0 <= r < N and 0 <= c < N and house[r][c] != "*"


def bfs(sr, sc, er, ec):
    dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    dq = deque()
    for d in range(4):
        dist[sr][sc][d] = 0
        dq.append((sr, sc, d))

    while dq:
        r, c, d = dq.popleft()
        nr, nc = r + dr[d], c + dc[d]
        
        if not can_pass(nr, nc):
            continue

        cur_dist = dist[r][c][d]
        # 직진
        if cur_dist < dist[nr][nc][d]:
            dist[nr][nc][d] = cur_dist
            dq.appendleft((nr, nc, d))

        # 거울 놓을 수 있는 곳
        if house[nr][nc] == "!":
            nd1 = (d + 1) % 4
            nd2 = (d - 1) % 4
            for nd in [(d + 1) % 4, (d - 1) % 4]:
                if cur_dist + 1 < dist[nr][nc][nd]:
                    dist[nr][nc][nd] = cur_dist + 1
                    dq.append((nr, nc, nd))

    return min(dist[er][ec])


print(bfs(*start, *end))
