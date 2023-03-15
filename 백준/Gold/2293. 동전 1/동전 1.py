# 백준 2293. 동전 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = [0 for _ in range(n)]

for i in range(n):
    coin[i] = int(input())

dp = [0 for _ in range(k + 1)]  # k원을 만드는 방법의 수

dp[0] = 1

for i in range(n):
    for j in range(1, k + 1):   # 1원에서 k원까지
        if j >= coin[i]:      # 동전 하나 가치보다 큰 금액이면
            dp[j] += dp[j - coin[i]]    # j에서 동전 가치 뺀 금액을 만드는 방법의 수를 더함.
            # (j - coin[i])를 만들고 거기에 coin[i] 동전을 하나 더 더하는 방법

print(dp[k])