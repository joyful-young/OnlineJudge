# 14442. 벽 부수고 이동하기 2
import sys
from collections import deque
input = sys.stdin.readline

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M, K = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

# visited[i][j][k]: (i+1, j+1)까지 벽을 k번 부수고 가는 최단거리
visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def bfs():
    q = deque([(0, 0, 0)])
    while q:
        ni, nj, k = q.popleft()
        if ni == N - 1 and nj == M - 1:
            return visited[N - 1][M - 1][k]

        for di, dj in directions:
            xi, xj = ni + di, nj + dj
            if not (0 <= xi < N and 0 <= xj < M):
                continue

            if arr[xi][xj] == "0" and visited[xi][xj][k] == 0:
                visited[xi][xj][k] = visited[ni][nj][k] + 1
                q.append((xi, xj, k))
            elif arr[xi][xj] == "1" and k < K and visited[xi][xj][k + 1] == 0:
                visited[xi][xj][k + 1] = visited[ni][nj][k] + 1
                q.append((xi, xj, k + 1))
    return -1

print(bfs())