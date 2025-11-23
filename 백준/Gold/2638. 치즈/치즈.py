import sys
from collections import deque


input = sys.stdin.readline
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def check_outside(start):
    dq = deque(start)
    while dq:
        r, c = dq.popleft()

        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                dq.append((nr, nc))
    return


def melt():
    melted = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                cnt = 0
                for dr, dc in DIR:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 2:
                        cnt += 1
                if cnt >= 2:
                    melted.append((r, c))

    for r, c in melted:
        arr[r][c] = 2
    return melted


# 외부 공기 체크
arr[0][0] = 2
check_outside([(0, 0)])


time = 0
while True:
    # 외부공기에 두 면 이상 노출된 치즈 녹이기
    melted_cheese = melt()
    if not melted_cheese:
        # 녹은 치즈 없으면 
        break
    time += 1

    # 치즈 녹은 후 외부 공기 업데이트
    check_outside(melted_cheese)

print(time)