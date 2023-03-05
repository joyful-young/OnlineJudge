# 백준 14500. 테트로미노

import sys
input = sys.stdin.readline


def get_sum(x1, y1, x2, y2):
    return pre_sum[x2][y2] - pre_sum[x2][y1] - pre_sum[x1][y2] + pre_sum[x1][y1]


def check1(maxV):
    # 가로 방향 확인
    for i in range(N):
        for j in range(3, M):
            maxV = max(maxV, get_sum(i - 1, j - 4, i, j))
    # 세로 방향 확인
    for j in range(M):
        for i in range(3, N):
            maxV = max(maxV, get_sum(i - 4, j - 1, i, j))
    return maxV


def check2(maxV):
    # 정사각형 확인
    for i in range(1, N):
        for j in range(1, M):
            maxV = max(maxV, get_sum(i - 2, j - 2, i, j))
    return maxV


def check3(maxV):
    # 3 x 2 확인 - L 모양, S 모양, T 모양
    for i in range(2, N):
        for j in range(1, M):
            tmp = get_sum(i - 3, j - 2, i, j)
            shape = [arr[i - 1][j] + arr[i - 2][j], arr[i - 2][j - 1] + arr[i - 1][j - 1],
                     arr[i - 1][j] + arr[i][j], arr[i][j - 1] + arr[i - 1][j - 1],
                     arr[i][j - 1] + arr[i - 2][j], arr[i - 2][j - 1] + arr[i][j],
                     arr[i - 2][j - 1] + arr[i][j - 1], arr[i - 2][j] + arr[i][j]]
            maxV = max(maxV, tmp - min(shape))

    # 2 x 3 확인
    for i in range(1, N):
        for j in range(2, M):
            tmp = get_sum(i - 2, j - 3, i, j)
            shape = [arr[i - 1][j - 2] + arr[i - 1][j - 1], arr[i][j - 2] + arr[i][j - 1],
                     arr[i - 1][j - 1] + arr[i - 1][j], arr[i][j - 1] + arr[i][j],
                     arr[i][j - 2] + arr[i - 1][j], arr[i - 1][j - 2] + arr[i][j],
                     arr[i - 1][j - 2] + arr[i - 1][j], arr[i][j - 2] + arr[i][j]]
            maxV = max(maxV, tmp - min(shape))
    return maxV


N, M = map(int, input().split())    # 행, 열

arr = [list(map(int, input().split())) for _ in range(N)]   # N x M 행렬

pre_sum = [[arr[i][j] for j in range(M)] + [0] for i in range(N)] + [[0 for _ in range(M + 1)]]

for i in range(N):
    for j in range(M):
        pre_sum[i][j] += pre_sum[i][j - 1]

for j in range(M):
    for i in range(N):
        pre_sum[i][j] += pre_sum[i - 1][j]

# print(pre_sum)

ans = check1(0)
ans = check2(ans)
ans = check3(ans)

print(ans)
