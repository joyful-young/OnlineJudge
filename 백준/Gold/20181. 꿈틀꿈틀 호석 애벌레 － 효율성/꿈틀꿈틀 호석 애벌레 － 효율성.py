import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))

s = 0
left = 0
right = 0
dp = [0] * (N + 1)
while right < N:
    right += 1
    s += arr[right]
    dp[right] = dp[right - 1]

    if s >= K:
        dp[right] = max(dp[right], dp[left] + s - K)
        while s >= K:
            left += 1
            s -= arr[left]

print(dp[N])