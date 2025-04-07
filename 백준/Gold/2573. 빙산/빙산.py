import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def count_adj_zero(xi, xj):
    """
    arr[xi][xj] != 0 인 경우에 사용
    """
    cnt = 0
    for i in range(4):
        ni, nj = xi + di[i], xj + dj[i]
        if arr[ni][nj] == 0:
            cnt += 1
    return cnt


def melt(ice):
    for i in range(len(ice)):
        r, c, h = ice[i]
        ice[i][2] = max(h - count_adj_zero(r, c), 0)

    remained_ice = []
    for r, c, h in ice:
        arr[r][c] = h
        if h != 0:
            remained_ice.append([r, c, h])
    return remained_ice


def check(si, sj, ice_cnt):
    q = deque([(si, sj)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[si][sj] = 1
    ice_cnt -= 1
    
    while q:
        xi, xj = q.popleft()

        for i in range(4):
            ni, nj = xi + di[i], xj + dj[i]
            if arr[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                ice_cnt -= 1

    # 붙은 얼음 확인하고 남은 얼음 있으면 분리된 것
    return ice_cnt != 0

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
current_ice = []
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(M):
        if arr[i][j] != 0:
            current_ice.append([i, j, arr[i][j]])

cnt = 0
while current_ice:
    current_ice = melt(current_ice)
    cnt += 1

    if not current_ice:
        print(0)
        break

    if check(current_ice[0][0], current_ice[0][1], len(current_ice)):
        print(cnt)
        break
    