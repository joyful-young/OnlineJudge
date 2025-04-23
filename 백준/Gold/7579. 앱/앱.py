import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

MAX_C = 10000

# dp[cost]: cost의 비용을 썼을 때 최대 확보 메모리
dp = [0 for _ in range(MAX_C + 1)]

for i in range(N):
    m, c = memories[i], costs[i]
    for cost in range(MAX_C, c - 1, -1):
        dp[cost] = max(dp[cost], dp[cost - c] + m)

for cost in range(MAX_C + 1):
    if dp[cost] >= M:
        print(cost)
        break
