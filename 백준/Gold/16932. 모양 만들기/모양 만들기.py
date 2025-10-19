import sys
from collections import deque


DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
shape_map = dict()


def bfs(sr, sc, number):
    visited[sr][sc] = True
    arr[sr][sc] = number
    cnt = 1

    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()

        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == 1:
                visited[nr][nc] = True
                arr[nr][nc] = number
                cnt += 1
                q.append((nr, nc))

    # {모양 번호: 모양의 크기}
    shape_map[number] = cnt
    return


def change(r, c):
    shapes = set()
    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0:
            # 인접한 모양들의 번호 set에 추가
            shapes.add(arr[nr][nc])

    return sum(shape_map[number] for number in shapes) + 1


shape_num = 2    # 모양 번호 2번부터 붙이기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs(i, j, shape_num)
            shape_num += 1

max_size = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            max_size = max(change(i, j), max_size)

print(max_size)