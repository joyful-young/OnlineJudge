import sys
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N = int(input())
min_h = 101
max_h = 0
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for h in tmp:
        if min_h > h:
            min_h = h
        if max_h < h:
            max_h = h


def dfs(sr, sc, h, visited):
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()

        if visited[r][c]:
            continue

        visited[r][c] = True

        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > h and not visited[nr][nc]:
                stack.append((nr, nc))
    return


def count_safe_zones(h):
    visited = [[False] * N for _ in range(N)]

    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > h:
                dfs(r, c, h, visited)
                cnt += 1
    return cnt

max_cnt = 1
for h in range(min_h, max_h):
    max_cnt = max(max_cnt, count_safe_zones(h))

print(max_cnt)