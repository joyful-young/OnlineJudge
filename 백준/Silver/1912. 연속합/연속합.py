# 백준 1912. 연속합

n = int(input())
num_lst = list(map(int, input().split()))

# dp[i]: i번째 원소까지 고려했을 때 i를 포함한 최대 연속합
# dp[i] = max(dp[i - 1] + num_lst[i], num_lst[i])
# (i-1)번째 원소가 포함된 최대 연속합 dp[i - 1]에 i번째 원소를 더하는 게 큰가, 아니면 그냥 i번째 원소가 큰가

dp = [0] * n
dp[0] = num_lst[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + num_lst[i], num_lst[i])

print(max(dp))