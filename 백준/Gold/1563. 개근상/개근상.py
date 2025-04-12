N = int(input())
DIV = 1000000

if N == 1:
    print(3)
elif N == 2:
    print(8)
else:
    # dp[L 포함 여부][AA, _A, __][n]
    # dp[0][0][n]: 전날까지 L 포함 x, 직전 출결 AA 일 때 개근상 받을 수 있는 경우의 수
    dp = [[[0 for _ in range(N + 1)] for _ in range(3)] for _ in range(2)]
    
    dp[0][0][3] = 1    # OAA
    dp[0][1][3] = 2    # OOA, AOA
    dp[0][2][3] = 4    # AAO, AOO, OAO, OOO
    dp[1][0][3] = 1    # LAA
    dp[1][1][3] = 3    # OLA, ALA, LOA
    dp[1][2][3] = 8    # OOL, OAL, AOL, AAL, LOO, LAO, OLO, ALO
    
    for i in range(4, N + 1):
        dp[0][0][i] = dp[0][1][i - 1]
        dp[0][1][i] = dp[0][2][i - 1]
        dp[0][2][i] = (dp[0][0][i - 1] + dp[0][1][i - 1] + dp[0][2][i - 1]) % DIV
        dp[1][0][i] = dp[1][1][i - 1]
        dp[1][1][i] = dp[1][2][i - 1]
    
        for j in range(2):
            for k in range(3):
                dp[1][2][i] += dp[j][k][i - 1]
        dp[1][2][i] %= DIV
    
    ans = 0
    for i in range(2):
        for j in range(3):
            ans += dp[i][j][N]
    print(ans % DIV)
