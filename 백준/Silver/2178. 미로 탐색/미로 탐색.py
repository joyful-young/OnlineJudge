import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

def bfs():
    q = deque([(0, 0)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1

    while q:
        xi, xj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = xi + di, xj + dj

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == "1" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[xi][xj] + 1

                if ni == N - 1 and nj == M - 1:
                    return visited[ni][nj]
    return visited[ni][nj]

print(bfs())