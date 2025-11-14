import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    Ri, Ci = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(Ri)])

notebook = [[0] * M for _ in range(N)]


def rotate(arr):
    return [list(col[::-1]) for col in zip(*arr)]


def is_valid(sr, sc, sticker):
    checked = []
    for dr in range(len(sticker)):
        for dc in range(len(sticker[0])):
            if sticker[dr][dc] == 1:
                if notebook[sr + dr][sc + dc] == 1:
                    return False
                
                checked.append((sr + dr, sc + dc))

    for r, c in checked:
        notebook[r][c] = 1
    return True


def stick(sticker):
    for r in range(N - len(sticker) + 1):
        for c in range(M - len(sticker[0]) + 1):
            if is_valid(r, c, sticker):
                return True
    return False


for sticker in stickers:
    cnt = 1
    while not stick(sticker) and cnt < 4:
        sticker = rotate(sticker)
        cnt += 1


print(sum(sum(row) for row in notebook))