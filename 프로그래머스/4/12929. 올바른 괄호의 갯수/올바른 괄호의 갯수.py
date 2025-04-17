def solution(n):
    dp = [0 for _ in range(15)]
    dp[0] = 1
    dp[1] = 1   # ()
    dp[2] = 2   # (()), ()()
    dp[3] = 5   # ((())), (()()), (())(), ()(()), ()()()
    
    if n < 4:
        return dp[n]
    
    # dp[i] = dp[i - 1] dp[0] + dp[i - 2] dp[1] + ... + dp[1] dp[i - 2] + dp[0] dp[i - 1]
    for i in range(4, n + 1):
        for j in range(i):
            dp[i] += dp[i - j - 1] * dp[j]
    return dp[n]
