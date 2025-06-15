import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [list(map(int, input().rstrip())) for _ in range(N)]

pre_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        pre_sum[i][j] += numbers[i - 1][j - 1] + pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1]

def get_sum(r1, c1, r2, c2):
    return pre_sum[r2][c2] - pre_sum[r1 - 1][c2] - pre_sum[r2][c1 - 1] + pre_sum[r1 - 1][c1 - 1]

max_v = 0
total = pre_sum[N][M]

for i in range(1, M - 1):
    for j in range(i + 1, M):
        a = get_sum(1, 1, N, i)
        b = get_sum(1, i + 1, N, j)
        c = get_sum(1, j + 1, N, M)
        max_v = max(max_v, a * b * c)

for i in range(1, N - 1):
    for j in range(i + 1, N):
        a = get_sum(1, 1, i, M)
        b = get_sum(i + 1, 1, j, M)
        c = get_sum(j + 1, 1, N, M)
        max_v = max(max_v, a * b * c)

for row in range(1, N):
    a = get_sum(1, 1, row, M)
    for col in range(1, M):
        b = get_sum(row + 1, 1, N, col)
        c = get_sum(row + 1, col + 1, N, M)
        max_v = max(max_v, a * b * c)

for col in range(1, M):
    a = get_sum(1, 1, N, col)
    for row in range(1, N):
        b = get_sum(1, col + 1, row, M)
        c = get_sum(row + 1, col + 1, N, M)
        max_v = max(max_v, a * b * c)

for row in range(1, N):
    for col in range(1, M):
        a = get_sum(1, 1, row, col)
        b = get_sum(1, col + 1, row, M)
        c = get_sum(row + 1, 1, N, M)
        max_v = max(max_v, a * b * c)

        b = get_sum(row + 1, 1, N, col)
        c = get_sum(1, col + 1, N, M)
        max_v = max(max_v, a * b * c)

print(max_v)