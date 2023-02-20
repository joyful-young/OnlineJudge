# 백준 13398. 연속합 2

n = int(input())
num_lst = list(map(int, input().split()))

# dp[0][i]: i번째 원소까지 고려했을 때 i번 원소를 포함한 최대 연속합
# dp[0][i] = max(dp[0][i - 1] + num_lst[i], num_lst[i])

# dp[1][i]: i번째 원소까지 고려했을 때, 수를 하나 제거했을 경우
# dp[1][i] = max(dp[1][i - 1] + num_lst[i], dp[0][i - 1])   이미 원소 하나를 제거해서 i번째 원소를 더하거나, i번째 원소 제거하거나

dp = [[0] * n for _ in range(2)]
dp[0][0] = num_lst[0]
dp[1][0] = 0        # 0번째 원소 제거하는 경우

ans = num_lst[0]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + num_lst[i], num_lst[i])
    dp[1][i] = max(dp[1][i - 1] + num_lst[i], dp[0][i - 1])
    ans = max(ans, dp[0][i], dp[1][i])

print(ans)