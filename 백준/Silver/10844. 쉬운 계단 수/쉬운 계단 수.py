N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
# dp[i][j]: j로 끝나는 i자리 계단 수 개수

dp[1] = [0] + [1] * 9

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]     # 0으로 끝나는 계단 수는 1로 끝나는 계단 수에 0 붙임
    dp[i][9] = dp[i - 1][8]     # 9로 끝나는 계산 수는 8로 끝나는 계단 수에 9
    for j in range(1, 9):       # j: 1 ~ 8. 각각 2가지 방법
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])

print(sum(dp[N]) % 1000000000)