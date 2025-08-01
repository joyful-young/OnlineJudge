import sys
input = sys.stdin.readline


MAX_DIFF = 1000000 * 1000
M, F = map(int, input().split())
m_personality = list(map(int, input().split()))
f_personality = list(map(int, input().split()))

# 오름차순 정렬
m_personality.sort()
f_personality.sort()

if M <= F:
    dp = [[MAX_DIFF] * (F + 1) for _ in range(M + 1)]
    dp[0][0] = 0

    for i in range(M + 1):
        for j in range(F + 1):
            if i < M and j < F:
                diff = abs(m_personality[i] - f_personality[j])
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + diff)
            if j < F:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])
    print(dp[M][F])
else:
    dp = [[MAX_DIFF] * (M + 1) for _ in range(F + 1)]
    dp[0][0] = 0

    for i in range(F + 1):
        for j in range(M + 1):
            if i < F and j < M:
                diff = abs(f_personality[i] - m_personality[j])
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + diff)
            if j < M:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])
    print(dp[F][M])