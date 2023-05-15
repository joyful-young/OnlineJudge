# 백준 2294. 동전2
# 사용하는 동전의 개수가 최소가 되도록 - 동전 최소 개수 출력
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]      # 동전 종류

dp = [10001 for _ in range(k + 1)]      # dp[i]: 합을 i로 만드는 데 필요한 최소 동전 개수
dp[0] = 0

for i in range(1, k + 1):
    for coin in arr:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)    # (i - coin)에 coin의 가치를 갖는 동전 하나를 더한 것과 비교

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])