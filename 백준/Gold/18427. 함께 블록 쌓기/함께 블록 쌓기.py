import sys
input = sys.stdin.readline

DIV = 10007
N, M, H = map(int, input().split())
blocks = [[0] + list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(H + 1)] for _ in range(N)]

for block in blocks[0]:
    if block <= H:
        dp[0][block] = 1

for student in range(1, N):
    for h in range(H + 1):
        for block in blocks[student]:
            prev_h = h - block
            if 0 <= prev_h <= H:
                dp[student][h] += dp[student - 1][prev_h]
                dp[student][h] %= DIV

print(dp[N - 1][H])