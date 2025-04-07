import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]

groups = []
visited = [[0 for _ in range(N)] for _ in range(N)]

def dfs(si, sj):
    stack = [(si, sj)]
    cnt = 0

    while stack:
        xi, xj = stack.pop()
        if visited[xi][xj] != 0:
            continue

        visited[xi][xj] = 1
        cnt += 1
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = xi + di, xj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != "0" and visited[ni][nj] == 0:
                stack.append((ni, nj))
    return cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] == "1" and visited[i][j] == 0:
            groups.append(dfs(i, j))

print(len(groups))
print(*sorted(groups), sep="\n")