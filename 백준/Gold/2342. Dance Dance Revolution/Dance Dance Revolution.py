INF = float('inf')

cmd = list(map(int, input().split()))
N = len(cmd[:-1])    # 마지막 0 제외


def cost(a, b):
    # 발을 a->b로 옮길 때 드는 힘
    if a == b:
        return 1
    if a == 0:
        return 2
    if abs(a - b) == 2:
        return 4
    return 3


# dp[l][r][i]: i개의 명령 후 왼발 l, 오른발 r에 있을 때 최소 힘
dp = [[[INF] * (N + 1) for _ in range(5)] for _ in range(5)]
dp[0][0][0] = 0


for i in range(1, N + 1):
    # 눌러야 할 번호 
    x = cmd[i - 1]
    for l in range(5):
        for r in range(5):
            prev = dp[l][r][i - 1]
            if prev == INF:
                continue

            dp[x][r][i] = min(dp[x][r][i], prev + cost(l, x))
            dp[l][x][i] = min(dp[l][x][i], prev + cost(r, x))

print(min(dp[l][r][N] for l in range(5) for r in range(5)))

