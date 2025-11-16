import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 행, 열
M, N = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]

# dp[r][c]: (r, c)부터 도착점(M - 1, N - 1)까지 가는 경로의 수
dp = [[-1] * N for _ in range(M)]
dp[M - 1][N - 1] = 1


def solve(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    
    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and heights[nr][nc] < heights[r][c]:
            # (r, c)에서 (nr, nc)로 이동 가능할 경우
            dp[r][c] += solve(nr, nc)
            
    return dp[r][c]

print(solve(0, 0))