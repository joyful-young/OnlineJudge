# 백준 1535. 안녕
# 평범한 배낭이랑 비슷하다

import sys
input = sys.stdin.readline


N = int(input())

hp = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))

# print(lose, gain)

dp = [[0] * 100 for _ in range(N + 1)]      # 0에서 99까지 소모체력. 0 ~ N 사람 수.

# dp[i][j] i번째 사람까지 갔을 때 j만큼의 체력을 소모하고 얻은 최대 기쁨

for i in range(1, N + 1):
    for j in range(1, 100):        # 체력 0 되면 안 됨. 잃는 체력은 자연수. 99
        if j < hp[i]:       # 잃을 체력이 허용치보다 크면 인사 안 함
            dp[i][j] = dp[i - 1][j]
        else:
            # 잃을 체력이 허용치보다 크지 않으면 i-1번째까지의 최대 기쁨과
            # 이전의 한 명을 선택하지 않고 i번째 사람 선택해 얻을 기쁨을 비교해 max값
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hp[i]] + happiness[i])

print(dp[N][99])