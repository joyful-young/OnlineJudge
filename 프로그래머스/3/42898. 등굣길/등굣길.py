DIV = 1000000007

def solution(m, n, puddles):
    puddles = set(map(tuple, puddles))
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j, i) not in puddles:
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
                dp[i][j] %= DIV
    print(dp)
    return dp[n][m]