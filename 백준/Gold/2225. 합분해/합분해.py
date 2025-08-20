N, K = map(int, input().split())

MOD = 1_000_000_000
dp = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(N + 1):
    dp[n][1] = 1
    
for k in range(1, K + 1):
    dp[0][k] = 1

for k in range(2, K + 1):
    for n in range(1, N + 1):
        dp[n][k] = (dp[n][k - 1] + dp[n - 1][k]) % MOD

print(dp[N][K])