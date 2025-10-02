import sys
input = sys.stdin.readline

D = {
    1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
    2: [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [
        [(0, -1), (-1, 0), (0, 1)], 
        [(-1, 0), (0, 1), (1, 0)], 
        [(0, 1), (1, 0), (0, -1)],
        [(1, 0), (0, -1), (-1, 0)]
    ],
    5: [[(0, -1), (-1, 0), (0, 1), (1, 0)]]
}


def monitor(ty, r, c):
    # (r, c)에 위치한 ty 종류의 cctv가 감시하는 영역
    monitored = []
    for directions in D[ty]:
        tmp = set()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 6:
                if grid[nr][nc] == 0:
                    tmp.add((nr, nc))
                nr += dr
                nc += dc
        monitored.append(tmp)
    return monitored


def bt(x, k, current_monitored):
    global max_v
    if x == k:
        # 감시되는 영역 세기
        max_v = max(max_v, len(current_monitored))
        return

    # x번 cctv 방향 정해 감시 영역 확인
    for area_set in monitored_area[x]:
        bt(x + 1, k, current_monitored.union(area_set))


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 0인 공간 개수
empty_area = 0
cctv = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            empty_area += 1
            continue

        if grid[i][j] != 6:
            cctv.append((grid[i][j], i, j))

# 각 cctv의 방향별 감시 영역 좌표 구하기
monitored_area = [monitor(*elem) for elem in cctv]

# 감시되는 영역 최대 개수
max_v = 0
bt(0, len(cctv), set())

# 사각지대 최소 개수
print(empty_area - max_v)