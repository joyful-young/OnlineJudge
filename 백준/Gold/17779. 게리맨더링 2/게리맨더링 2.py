import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
pre_sum = [[0] * (N + 1) for _ in range(N + 1)]    # 1-index

for i in range(1, N + 1):
    for j in range(1, N + 1):
        pre_sum[i][j] = arr[i - 1][j - 1] + pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1]

total = pre_sum[N][N]

def get_sum(r1, c1, r2, c2):
    return pre_sum[r2][c2] - pre_sum[r1 - 1][c2] - pre_sum[r2][c1 - 1] + pre_sum[r1 - 1][c1 - 1]

def get_popularity_diff(x, y, d1, d2):
    # 1번
    row = x + d1 - 1
    col = y - d1
    s1 = get_sum(1, 1, row, col)
    while row > 1 and col < y:
        row -= 1
        col += 1
        s1 += get_sum(1, col, row, col)
        
    # 2번
    row = x
    col = y + 1
    s2 = get_sum(1, col, row, N)
    while col < N and row < x + d2:
        row += 1
        col += 1
        s2 += get_sum(row, col, row, N)

    # 3번
    row = x + d1 + d2
    col = y - d1 + d2 - 1
    s3 = get_sum(row, 1, N, col)
    while col > 1 and row > x + d1:
        row -= 1
        col -= 1
        s3 += get_sum(row, 1, row, col)

    # 4번
    row = x + d2 + 1
    col = y + d2
    s4 = get_sum(row, col, N, N)
    while row < N and col > y - d1 + d2:
        row += 1
        col -= 1
        s4 += get_sum(row, col, N, col)

    # 5번
    s5 = total - (s1 + s2 + s3 + s4)

    # 최대 - 최소
    s = [s1, s2, s3, s4, s5]
    return max(s) - min(s)


get_popularity_diff(3, 3, 1, 1)


# 선거구 인구차 최솟값
answer = total
for r in range(1, N - 1):
    for c in range(2, N):
        for l1 in range(1, c):
            for l2 in range(1, N - c + 1):
                if l1 + l2 > N - r:
                    continue

                answer = min(get_popularity_diff(r, c, l1, l2), answer)

print(answer)