import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R = 12
C = 6
fields = [list(input().rstrip()) for _ in range(R)]
puyo = []

# 열 작은 것, 행 큰 것부터
for j in range(C):
    for i in range(R - 1, -1, -1):
        if fields[i][j] != ".":
            puyo.append((i, j, fields[i][j]))

def bfs(r, c, v, visited):
    visited[r][c] = 1
    q = deque([(r, c)])
    same_colors = set([(r, c)])
    while q:
        xr, xc = q.popleft()

        for d in range(4):
            nr, nc = xr + dr[d], xc + dc[d]
            if 0 <= nr < R and 0 <= nc < C and fields[nr][nc] == v and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                same_colors.add((nr, nc))
                q.append((nr, nc))

    if len(same_colors) >= 4:
        return same_colors
    return []


def burst():
    if not puyo:
        return False
    flag = False
    visited = [[0 for _ in range(C)] for _ in range(R)]
    burst_puyo = set()
    for r, c, v in puyo:
        if not visited[r][c]:
            same_colors = bfs(r, c, v, visited)
            if same_colors:
                flag = True
                burst_puyo.update(same_colors)
    # 터질 게 없을 경우
    if not flag:
        return False

    # 터짐
    for r, c in burst_puyo:
        fields[r][c] = "."
        
    # puyo - 열 오름차순, 행 내림차순으로 정렬된 상태
    puyo_dict = {}
    for r, c, v in puyo:
        if (r, c) not in burst_puyo:
            if c in puyo_dict:
                puyo_dict[c].append((r, v))
            else:
                puyo_dict[c] = [(r, v)]

    puyo.clear()
    for c in puyo_dict:
        col_c_puyos = puyo_dict[c]
        for i in range(len(col_c_puyos)):
            r, v = col_c_puyos[i]
            new_r = R - i - 1
            fields[r][c] = "."
            fields[new_r][c] = v
            puyo.append((new_r, c, v))
    return True

ans = 0
while burst():
    ans += 1
print(ans)
