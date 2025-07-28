import sys
from collections import deque
input = sys.stdin.readline


DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
dist = [[[N * M + 1 for _ in range(M)] for _ in range(N)] for _ in range(2)]
dist[0][0][0] = 1


def bfs(sr, sc):
    dq = deque([(sr, sc, 0)])
    visited[0][sr][sc] = True
    
    while dq:
        r, c, broke = dq.popleft()

        if r == N - 1 and c == M - 1:
            return dist[broke][r][c]

        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == "0" and not visited[broke][nr][nc]:
                    visited[broke][nr][nc] = True
                    dist[broke][nr][nc] = dist[broke][r][c] + 1
                    dq.append((nr, nc, broke))
                elif arr[nr][nc] == "1" and broke == 0 and not visited[1][nr][nc]:
                    visited[1][nr][nc] = True
                    dist[1][nr][nc] = dist[0][r][c] + 1
                    dq.append((nr, nc, 1))

    return -1

print(bfs(0, 0))