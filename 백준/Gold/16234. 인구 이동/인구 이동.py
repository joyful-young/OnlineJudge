import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def move():
    groups = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                group = find_group(i, j, visited)
                if len(group) > 1:
                    groups.append(group)

    if not groups:
        return False
    
    for group in groups:
        population = sum([arr[r][c] for r, c in group]) // len(group)
        for r, c in group:
            arr[r][c] = population
    return True


def find_group(si, sj, visited):
    stack = [(si, sj)]
    visited[si][sj] = 1
    group = [(si, sj)]
    while stack:
        xi, xj = stack.pop()

        for i in range(4):
            ni, nj = xi + di[i], xj + dj[i]
            if not (0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0):
                continue
            if L <= abs(arr[xi][xj] - arr[ni][nj]) <= R:
                visited[ni][nj] = 1
                stack.append((ni, nj))
                group.append((ni, nj))
    return group


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

day = 0
while move():
    day += 1
print(day)