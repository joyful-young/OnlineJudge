import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def spread(empty_place_cnt):
    global safety_zone
    after_build_wall = [[arr[i][j] for j in range(M)] for i in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for r, c in virus:
        visited[r][c] = 1
    q = deque(virus)
    while q:
        xi, xj = q.popleft()

        for i in range(4):
            ni, nj = xi + di[i], xj + dj[i]
            if 0 <= ni < N and 0 <= nj < M and after_build_wall[ni][nj] == 0 and visited[ni][nj] == 0:
                empty_place_cnt -= 1
                if empty_place_cnt < safety_zone:
                    return empty_place_cnt
                visited[ni][nj] = 1
                after_build_wall[ni][nj] = 2
                q.append((ni, nj))

    return empty_place_cnt

def build_wall(n, r, s):
    # n: 빈 공간 개수, r: 세워야 할 벽의 수
    # s: empty 배열에서 선택 가능한 최초 요소 인덱스
    global safety_zone
    if r == 0:
        # 벽 모두 세운 후
        safety_zone = max(safety_zone, spread(n - 3))
        return

    for i in range(s, n - r + 1):
        wi, wj = empty[i]
        arr[wi][wj] = 1
        build_wall(n, r - 1, i + 1)
        arr[wi][wj] = 0

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
empty = []
virus = []
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

safety_zone = 0
build_wall(len(empty), 3, 0)
print(safety_zone)

