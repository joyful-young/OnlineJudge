# 1937. 욕심쟁이 판다
import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
# dp[i][j]: i행 j열로부터 이동 가능한 칸의 수 최댓값

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(si, sj):
    stack = [[si, sj, 0, 1]]    # 행, 열, 이동 방향 인덱스, 현재까지 계산된 이동 가능 칸수 최댓값

    while stack:
        r, c, dr, current_max = stack[-1]

        if dp[r][c] != -1:  # dp값 이미 결정. 이전 칸 업데이트
            stack.pop()
            if stack:
                stack[-1][3] = max(stack[-1][3], dp[r][c] + 1)
            continue

        if dr < 4:  # 아직 확인하지 않은 방향 남았을 경우
            stack[-1][2] += 1
            ni, nj = r + directions[dr][0], c + directions[dr][1]

            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > arr[r][c]:
                if dp[ni][nj] != -1:
                    stack[-1][3] = max(stack[-1][3], dp[ni][nj] + 1)
                else:
                    stack.append([ni, nj, 0, 1])
        else:   # 모든 방향 확인 완료. dp 값 결정
            dp[r][c] = stack[-1][3]
            stack.pop()
            if stack:
                stack[-1][3] = max(stack[-1][3], dp[r][c] + 1)

    return dp[si][sj]


ans = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dfs(i, j)
        ans = max(ans, dp[i][j])

# print(dp)
print(ans)