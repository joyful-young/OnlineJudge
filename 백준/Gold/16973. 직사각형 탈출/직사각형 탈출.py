import sys
from collections import deque
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]    # 0-index
H, W, Sr, Sc, Fr, Fc = map(int, input().split())   # 1-index

pre_sum = [[0] * (M + 1) for _ in range(N + 1)]    # 1-index
for i in range(1, N + 1):
    for j in range(1, M + 1):
        pre_sum[i][j] = arr[i - 1][j - 1] + pre_sum[i][j - 1] + pre_sum[i - 1][j] - pre_sum[i - 1][j - 1]

def get_sum(lr, lc, rr, rc):
    return pre_sum[rr][rc] - pre_sum[rr][lc - 1] - pre_sum[lr - 1][rc] + pre_sum[lr - 1][lc - 1]

MAX_V = 1001
visited = [[MAX_V] * (M + 1) for _ in range(N + 1)]    # 1-index
visited[Sr][Sc] = 0


def can_move(lr, lc):
    if not (1 <= lr <= N and 1 <= lc <= M and visited[lr][lc] == MAX_V):
        return False
    
    rr = lr + H - 1
    rc = lc + W - 1
    if not (1 <= rr <= N and 1 <= rc <= M):
        return False

    return get_sum(lr, lc, rr, rc) == 0


q = deque([(Sr, Sc)])
while q:
    r, c = q.popleft()

    if r == Fr and c == Fc:
        break

    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if can_move(nr, nc):
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

print(visited[Fr][Fc] if visited[Fr][Fc] != MAX_V else -1)