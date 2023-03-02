# 백준 2583. 영역 구하기

import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs(si, sj):
    global cnt
    cnt += 1
    stack = [(si, sj)]  # 출발점 push
    arr[si][sj] = 1     # 방문 표시
    area_tmp = 0        # 면적 초기화

    while stack:
        ci, cj = stack.pop()
        area_tmp += 1
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
                stack.append((ni, nj))
                arr[ni][nj] = 1
    return area_tmp


M, N, K = map(int, input().split())     # 행, 열, 분리 영역

arr = [[0 for _ in range(N)] for _ in range(M)]

# 직사각형 칠하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())      # x좌표가 열 방향, y좌표가 행 방향

    for i in range(M):
        for j in range(N):
            if y1 <= i < y2 and x1 <= j < x2:
                arr[i][j] = 1

# 분리된 영역 개수와 넓이 구하기
cnt = 0
area = list()
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            area.append(dfs(i, j))

print(cnt)
print(*sorted(area))