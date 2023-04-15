# 백준 9251. LCS

str1 = input()
str2 = input()
N = len(str1)
M = len(str2)

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
# str1의 i번째 문자, str2의 j번째 문자까지 확인했을 때의 최장공통수열 길이

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if str1[i - 1] == str2[j - 1]:      # 두 문자가 같으면
            dp[i][j] = dp[i - 1][j - 1] + 1     # 왼쪽 대각선 윗칸에 1 더함
        else:                               # 두 문자가 다르면
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 윗칸이나 왼쪽칸의 값 중 큰 값

print(dp[N][M])