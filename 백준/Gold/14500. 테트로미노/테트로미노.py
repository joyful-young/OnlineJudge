import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]
pre_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        pre_sum[i][j] = numbers[i - 1][j - 1] + pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1]

regular_sum = lambda r1, c1, r2, c2: pre_sum[r2][c2] - pre_sum[r1 - 1][c2] - pre_sum[r2][c1 - 1] + pre_sum[r1 - 1][c1 - 1]

def put_type1():
    # 막대 모양
    # 가로로
    max_v = 0
    for i in range(1, N + 1):
        for j in range(1, M - 2):
            max_v = max(max_v, regular_sum(i, j, i, j + 3))
    # 세로로
    for i in range(1, N - 2):
        for j in range(1, M + 1):
            max_v = max(max_v, regular_sum(i, j, i + 3, j))
    return max_v


def put_type2():
    # 정사각형 모양
    max_v = 0
    for i in range(1, N):
        for j in range(1, M):
            max_v = max(max_v, regular_sum(i, j, i + 1, j + 1))
    return max_v


def put_type3():
    # 3 x 2
    max_v = 0
    for i in range(1, N - 1):
        for j in range(1, M):
            temp = regular_sum(i, j, i + 2, j + 1)
            blank = [
                # L 모양
                numbers[i - 1][j] + numbers[i][j],
                numbers[i][j] + numbers[i + 1][j],
                numbers[i][j - 1] + numbers[i + 1][j - 1],
                numbers[i - 1][j - 1] + numbers[i][j - 1],
                # S 모양
                numbers[i - 1][j] + numbers[i + 1][j - 1],
                numbers[i - 1][j - 1] + numbers[i + 1][j],
                # T 모양
                numbers[i - 1][j - 1] + numbers[i + 1][j - 1],
                numbers[i - 1][j] + numbers[i + 1][j]
            ]
            max_v = max(max_v, temp - min(blank))

    # 2 x 3
    for i in range(1, N):
        for j in range(1, M - 1):
            temp = regular_sum(i, j, i + 1, j + 2)
            blank = [
                # L 모양
                numbers[i - 1][j - 1] + numbers[i - 1][j],
                numbers[i][j] + numbers[i][j + 1],
                numbers[i][j - 1] + numbers[i][j],
                numbers[i - 1][j] + numbers[i - 1][j + 1],
                # S 모양
                numbers[i - 1][j - 1] + numbers[i][j + 1],
                numbers[i - 1][j + 1] + numbers[i][j - 1],
                # T 모양
                numbers[i][j - 1] + numbers[i][j + 1],
                numbers[i - 1][j - 1] + numbers[i - 1][j + 1]
            ]
            max_v = max(max_v, temp - min(blank))
    return max_v

print(max(put_type1(), put_type2(), put_type3()))
