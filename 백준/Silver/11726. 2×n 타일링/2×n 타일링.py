# 백준 11726. 2 x n 타일링
# dp[n] = dp[n - 2] + dp[n - 1]
# n-2 채우고 가로 두 줄 놓거나 n-1 채우고 세로로 하나 더 붙이기

N = int(input())

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

print(dp[N])
