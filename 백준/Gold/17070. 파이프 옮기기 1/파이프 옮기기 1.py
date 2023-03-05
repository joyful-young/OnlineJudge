# 백준 17070. 파이프 옮기기1

N = int(input())

arr = [[1 for _ in range(N + 2)]]\
      + [[1] + list(map(int, input().split())) + [1] for _ in range(N)]\
      + [[1 for _ in range(N + 2)]]     # 가장자리 1로 둘러싸기
# 원본은 1 ~ N

# (i, j)에 가로로 와서 도착, 세로로 와서 도착, 대각선으로 와서 도착
dp = [[[0 for _ in range(N + 2)] for _ in range(N + 2)] for _ in range(3)]
# print(arr)
# print(dp)

dp[0][1][2] = 1     # (1, 2)에 파이프의 끝이 가로로 놓여 있음

for j in range(3, N + 1):
    if arr[1][j] == 0:      # 1행에서는 벽이 아닌 곳에 가로로만 갈 수 있음
        dp[0][1][j] = dp[0][1][j - 1]

for i in range(2, N + 1):
    for j in range(3, N + 1):
        if arr[i][j] == 0:      # 벽이 아니면
            # 가로로 오는 법은 (i, j - 1)에 가로로 오거나 대각선으로 오는 법의 합
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]

            # 세로로 오는 법은 (i - 1, j)에 세로로 오거나 대각선으로 오는 법의 합
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

        if arr[i][j] == 0 and arr[i - 1][j] == 0 and arr[i][j - 1] == 0:
            # 대각선으로 오는 법은 (i - 1, j - 1)에 가로, 세로, 대각선으로 오는 법의 합
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

# print(dp)
print(dp[0][N][N] + dp[1][N][N] + dp[2][N][N])  # (N, N)으로 옮기는 방법의 총합
