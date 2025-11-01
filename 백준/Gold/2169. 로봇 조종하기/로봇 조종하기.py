import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

dp[0][0] = arr[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + arr[0][j]

for i in range(1, N):
    l_to_r = [0] * M
    l_to_r[0] = dp[i - 1][0] + arr[i][0]
    for j in range(1, M):
        l_to_r[j] = max(l_to_r[j - 1], dp[i - 1][j]) + arr[i][j]

    if i == N - 1:
        dp[i] = l_to_r[::]
        break

    r_to_l = [0] * M
    r_to_l[-1] = dp[i - 1][-1] + arr[i][-1]
    for j in range(M - 2, -1, -1):
        r_to_l[j] = max(r_to_l[j + 1], dp[i - 1][j]) + arr[i][j]

    for j in range(M):
        dp[i][j] = max(l_to_r[j], r_to_l[j])

print(dp[N - 1][M - 1])