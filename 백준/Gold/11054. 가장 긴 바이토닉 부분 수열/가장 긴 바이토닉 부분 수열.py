import sys
input = sys.stdin.readline

N = int(input())
series = list(map(int, input().split()))

dp = [[1] * N for _ in range(2)]
for i in range(N):
    for j in range(i):
        if series[i] > series[j]:
            # 감소한 적 있는 건 안 됨
            dp[0][i] = max(dp[0][j] + 1, dp[0][i])
        elif series[i] < series[j]:
            dp[1][i] = max(dp[0][j] + 1, dp[1][j] + 1, dp[1][i])

print(max(max(dp[0]), max(dp[1])))