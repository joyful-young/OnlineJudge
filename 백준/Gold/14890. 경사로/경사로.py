import sys
input = sys.stdin.readline

def can_pass(road):
    n = len(road)
    go_up = []    # (i - 1)보다 하나 올라가는 i
    go_down = []  # (i - 1)보다 하나 내려가는 i
    for i in range(1, n):
        diff = road[i] - road[i - 1]
        if abs(diff) > 1:
            return False

        if diff == 1:
            go_up.append(i)
        elif diff == -1:
            go_down.append(i)

    # 인접한 칸과의 높이차가 1 이하인 경우만 남음
    # 경사로 놓아진 곳 표시
    placed = [False for _ in range(n)]
    for i in go_up:
        if i < L or placed[i - 1]:
            return False
        placed[i - 1] = True
        for j in range(i - L, i - 1):
            if road[j] != road[i - 1] or placed[j]:
                return False
            else:
                placed[j] = True

    for i in go_down:
        if i > n - L or placed[i]:
            return False
        placed[i] = True
        for j in range(i + 1, i + L):
            if road[j] != road[i] or placed[j]:
                return False
            else:
                placed[j] = True
    return True


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
transposed = [list(row) for row in zip(*arr)]

cnt = 0
for row in arr:
    if can_pass(row):
        cnt += 1
for row in transposed:
    if can_pass(row):
        cnt += 1
print(cnt)