N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(N + 1):
    dp[n][1] = 1

for k in range(1, K + 1):
    for n in range(N + 1):
        for i in range(n + 1):
            dp[n][k] += dp[n - i][k - 1]
            dp[n][k] %= 1000000000

print(dp[N][K])