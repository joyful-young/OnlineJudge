def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    return dp[n]