def solution(n, tops):
    # dp[i][0]: i+1 번째 정삼각형까지 타일링. 오른쪽 끝이 삼각형으로 끝나도록 채워질 때
    # dp[i][1]: 오른쪽 끝이 마름모로 끝나도록 채워질 때
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 3 if tops[0] == 1 else 2
    dp[0][1] = 1
    
    for i in range(1, n):
        if tops[i] == 1:
            dp[i][0] = (3 * dp[i - 1][0] + 2 * dp[i - 1][1]) % 10007
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % 10007
        else:
            dp[i][0] = (2 * dp[i - 1][0] + dp[i - 1][1]) % 10007
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % 10007
            
    return sum(dp[n - 1]) % 10007