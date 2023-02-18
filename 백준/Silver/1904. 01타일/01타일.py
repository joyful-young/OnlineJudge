# 백준 1904. 01타일
# dp[n] = dp[n - 2] + dp[n - 1]
# (n-2)자리 수에 00을 붙이거나 (n-1)자리 수에 1을 붙이거나

N = int(input())

dp = [0] * (N + 1)      # N자리수 만들 수 있는 가짓수
dp[0] = 1
dp[1] = 1
# dp[2] = 2
# dp[3] = 3

for i in range(2, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746     # 나머지 연산. 덧셈 분배법칙 성립

print(dp[N])