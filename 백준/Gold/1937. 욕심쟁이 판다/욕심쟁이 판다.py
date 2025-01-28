# 1937. 욕심쟁이 판다
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(row, col):
    if dp[row][col] != -1:
        return dp[row][col]

    bamboo = arr[row][col]
    max_value = 1
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        xi, xj = row + di, col + dj
        if 0 <= xi < n and 0 <= xj < n and arr[xi][xj] > bamboo:
            max_value = max(max_value, dfs(xi, xj) + 1)
    dp[row][col] = max_value
    return dp[row][col]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
# dp[i][j] i행 j열로부터 이동 가능한 칸의 수 최댓값

ans = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            ans = max(ans, dfs(i, j))

# print(dp)
print(ans)