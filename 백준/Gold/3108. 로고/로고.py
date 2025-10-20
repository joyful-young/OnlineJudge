import sys
input = sys.stdin.readline

N = int(input())
rectangles = [(0, 0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
rep = [i for i in range(N + 1)]


def find(x):
    if rep[x] == x:
        return x

    rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep_x, rep_y = find(x), find(y)

    if rep_x <= rep_y:
        rep[rep_y] = rep_x
    else:
        rep[rep_x] = rep_y


def is_overlapping(r1, r2):
    x1, y1, x2, y2 = rectangles[r1]
    x3, y3, x4, y4 = rectangles[r2]

    # 아예 떨어져 있는 경우
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return False

    # 한쪽이 다른 쪽의 내부에
    if (x1 > x3 and x2 < x4 and y1 > y3 and y2 < y4) or (x3 > x1 and x4 < x2 and y3 > y1 and y4 < y2):
        return False

    return True


# 그룹
for i in range(N):
    for j in range(i + 1, N + 1):
        if is_overlapping(i, j):
            union(i, j)


groups = set(find(i) for i in rep)
print(len(groups) - 1)
