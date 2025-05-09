DIV = 1000000007

def solution(m, n, puddles):
    # dp[i][j]: (j, i)로 가는 최단경로의 수 dp[i - 1][j] + dp[i][j - 1]
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    puddles_set = set(map(tuple, puddles))
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j, i) in puddles_set:
                continue
                
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
            dp[i][j] %= DIV
    return dp[n][m]