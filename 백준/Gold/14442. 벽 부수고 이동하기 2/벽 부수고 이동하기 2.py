# 14442. 벽 부수고 이동하기 2
import sys
from collections import deque
input = sys.stdin.readline

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M, K = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

# visited[i][j]: (i+1, j+1)에 도달하기까지 최단거리
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
# break_cnt[i][j]: (i+1, j+1)에 도달하기까지 벽을 부순 횟수
break_cnt = [[K + 1 for _ in range(M)] for _ in range(N)]
break_cnt[0][0] = 0
def bfs():
    q = deque([(0, 0)])
    while q:
        ni, nj = q.popleft()
        if ni == N - 1 and nj == M - 1:
            return visited[N - 1][M - 1]

        for di, dj in directions:
            xi, xj = ni + di, nj + dj
            if not (0 <= xi < N and 0 <= xj < M):
                continue

            if arr[xi][xj] == "0" and break_cnt[xi][xj] > break_cnt[ni][nj]:
                visited[xi][xj] = visited[ni][nj] + 1
                break_cnt[xi][xj] = break_cnt[ni][nj]
                q.append((xi, xj))
            elif arr[xi][xj] == "1" and break_cnt[ni][nj] < K and break_cnt[xi][xj] > break_cnt[ni][nj] + 1:
                visited[xi][xj] = visited[ni][nj] + 1
                break_cnt[xi][xj] = break_cnt[ni][nj] + 1
                q.append((xi, xj))
    return -1

print(bfs())