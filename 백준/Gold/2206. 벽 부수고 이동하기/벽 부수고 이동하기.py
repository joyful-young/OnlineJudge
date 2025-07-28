import sys
from collections import deque
input = sys.stdin.readline


DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

MAX_D = N * M + 1
visited = [[[MAX_D for _ in range(M)] for _ in range(N)] for _ in range(2)]
visited[0][0][0] = 1


def bfs(sr, sc):
    dq = deque([(sr, sc, 0)])
    
    while dq:
        r, c, broke = dq.popleft()

        if r == N - 1 and c == M - 1:
            return visited[broke][r][c]

        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == "0" and visited[broke][nr][nc] == MAX_D:
                    visited[broke][nr][nc] = visited[broke][r][c] + 1
                    dq.append((nr, nc, broke))
                elif arr[nr][nc] == "1" and broke == 0 and visited[1][nr][nc] == MAX_D:
                    visited[1][nr][nc] = visited[0][r][c] + 1
                    dq.append((nr, nc, 1))

    return -1

print(bfs(0, 0))