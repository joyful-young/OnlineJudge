import sys
input = sys.stdin.readline

# 이동 방향(0: 좌, 1: 하, 2: 우, 3: 상)
DIR = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}

P = (0.01, 0.01, 0.02, 0.02, 0.07, 0.07, 0.1, 0.1, 0.05)

def get_coords(r, c, direction):
    if direction == 0:
        # 오른쪽에서 왼쪽으로
        return (
            (r - 1, c + 1), (r + 1, c + 1),
            (r - 2, c), (r + 2, c),
            (r - 1, c), (r + 1, c),
            (r - 1, c - 1), (r + 1, c - 1),
            (r, c - 2),
            (r, c - 1)
        )
    elif direction == 1:
        # 위에서 아래로
        return (
            (r - 1, c - 1), (r - 1, c + 1),
            (r, c - 2), (r, c + 2),
            (r, c - 1), (r, c + 1),
            (r + 1, c - 1), (r + 1, c + 1),
            (r + 2, c),
            (r + 1, c)
        )
    elif direction == 2:
        # 왼쪽에서 오른쪽으로
        return (
            (r - 1, c - 1), (r + 1, c - 1),
            (r - 2, c), (r + 2, c),
            (r - 1, c), (r + 1, c),
            (r - 1, c + 1), (r + 1, c + 1),
            (r, c + 2),
            (r, c + 1)
        )
    else:
        # 아래에서 위로
        return (
            (r + 1, c - 1), (r + 1, c + 1),
            (r, c - 2), (r, c + 2),
            (r, c - 1), (r, c + 1),
            (r - 1, c - 1), (r - 1, c + 1),
            (r - 2, c),
            (r - 1, c)
        )


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 토네이도 시작점
nr = N // 2
nc = N // 2

# 한방향 이동 거리
n = 1
d = 0

out = 0

while (nr, nc) != (0, 0):
    for _ in range(n):
        nr += DIR[d][0]
        nc += DIR[d][1]

        coords = get_coords(nr, nc, d)
        temp_sum = 0
        for idx in range(len(P)):
            tr, tc = coords[idx]
            temp = int(sand[nr][nc] * P[idx])
            temp_sum += temp
            if 0 <= tr < N and 0 <= tc < N:
                sand[tr][tc] += temp
            else:
                out += temp

        ar, ac = coords[-1]
        if 0 <= ar < N and 0 <= ac < N:
            sand[ar][ac] += sand[nr][nc] - temp_sum
        else:
            out += sand[nr][nc] - temp_sum
        sand[nr][nc] = 0

        if (nr, nc) == (0, 0):
            break

    if d == 1:
        n += 1
    elif d == 3:
        n += 1
    d = (d + 1) % 4
print(out)
