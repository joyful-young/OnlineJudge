# 12865. 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i번째 물건까지 확인해서 배낭에 넣었을 때 무게가 j가 될 경우 물건 가치 최댓값
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = stuff[i - 1]
    for j in range(K + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            # i번째 물건을 넣지 않을 경우, i번째 물건을 넣을 경우를 비교하여 최댓값으로
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])
