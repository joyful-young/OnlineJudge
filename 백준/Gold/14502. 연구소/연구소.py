import sys
from collections import deque
input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def spread(empty_place_cnt):
    global safety_zone
    after_build_wall = [row[:] for row in arr]
    q = deque(virus)

    while q:
        xi, xj = q.popleft()
        for d in range(4):
            ni, nj = xi + di[d], xj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and after_build_wall[ni][nj] == 0:
                after_build_wall[ni][nj] = 2
                empty_place_cnt -= 1
                if empty_place_cnt < safety_zone:
                    return  # 더 이상 최댓값 갱신 불가, 가지치기
                q.append((ni, nj))

    safety_zone = max(safety_zone, empty_place_cnt)

def build_wall(n, r, s):
    if r == 0:
        spread(n - 3)
        return
    for i in range(s, n - r + 1):
        wi, wj = empty[i]
        arr[wi][wj] = 1
        build_wall(n, r - 1, i + 1)
        arr[wi][wj] = 0

# 입력 처리
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
