import sys
input = sys.stdin.readline


dr = [0, 1, 0, -1]    # 우하좌상
dc = [1, 0, -1, 0]


def adj_area(r, c):
    area = []
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
            area.append((nr, nc))
    return area


def diffuse():
    # 좌표: 확산 후 미세먼지 양
    after = {}
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                diffused_to = adj_area(r, c)
                diffused_amount = arr[r][c] // 5

                if (r, c) in after:
                    after[(r, c)] -= diffused_amount * len(diffused_to)
                else:
                    after[(r, c)] = arr[r][c] - (diffused_amount * len(diffused_to))

                for pos in diffused_to:
                    if pos in after:
                        after[pos] += diffused_amount
                    else:
                        after[pos] = arr[pos[0]][pos[1]] + diffused_amount

    # arr 반영
    total = 0
    for pos, amount in after.items():
        arr[pos[0]][pos[1]] = amount
        total += amount
    return total


def purify(dust_amount):
    global remained
    
    d = 3    # 3 -> 0 -> 1 -> 2
    pr, pc = purifiers[0][0] - 1, purifiers[1][1]
    nr, nc = pr - 1, pc
    dust_amount -= arr[pr][pc]
    while (nr, nc) != purifiers[0]:
        arr[pr][pc] = arr[nr][nc]
        pr, pc = nr, nc

        tr, tc = nr + dr[d], nc + dc[d]
        if 0 <= tr <= purifiers[0][0] and 0 <= tc < C:
            nr, nc = tr, tc
        else:
            d = (d + 1) % 4
            nr, nc = nr + dr[d], nc + dc[d]
    arr[pr][pc] = 0

    d = 1    # 1 -> 0 -> 3 -> 2
    pr, pc = purifiers[1][0] + 1, purifiers[1][1]
    nr, nc = pr + 1, pc
    dust_amount -= arr[pr][pc]
    while (nr, nc) != purifiers[1]:
        arr[pr][pc] = arr[nr][nc]
        pr, pc = nr, nc

        tr, tc = nr + dr[d], nc + dc[d]
        if purifiers[1][0] <= tr < R and 0 <= tc < C:
            nr, nc = tr, tc
        else:
            d = (d - 1) % 4
            nr, nc = nr + dr[d], nc + dc[d]
    arr[pr][pc] = 0
    
    remained = dust_amount

R, C, T = map(int, input().split())
arr = [0 for _ in range(R)]

purifiers = []
for r in range(R):
    arr[r] = list(map(int, input().split()))
    for c in range(C):
        if arr[r][c] == -1:
            purifiers.append((r, c))

remained = 0
for _ in range(T):
    purify(diffuse())
print(remained)
