import sys
input = sys.stdin.readline

cctv_dir = {
    1: [[(0, 1)], [(-1, 0)], [(0, -1)], [(1, 0)]],
    2: [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
    3: [[(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)], [(1, 0), (0, 1)]],
    4: [
        [(0, 1), (-1, 0), (0, -1)],
        [(-1, 0), (0, -1), (1, 0)],
        [(0, -1), (1, 0), (0, 1)],
        [(1, 0), (0, 1), (-1, 0)]
    ],
    5: [[(0, 1), (-1, 0), (0, -1), (1, 0)]]
}

def monitor(ty, r, c):
    monitored = []
    for dir_list in cctv_dir[ty]:
        temp = set()
        for dr, dc in dir_list:
            nr, nc = r + dr, c + dc
            while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 6:
                if arr[nr][nc] == 0:
                    temp.add((nr, nc))
                nr += dr
                nc += dc
        monitored.append(temp)
    return monitored

def count_monitored_area(x, k, monitored_area_set):
    global monitored_cnt
    if x == k:
        # 전체 cctv 방향 결정 완료
        monitored_cnt = max(monitored_cnt, len(monitored_area_set))
        return

    for area_set in monitored_area[x]:        
        count_monitored_area(x + 1, k, monitored_area_set.union(area_set))
    

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
area = 0
cctv = []
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(M):
        if arr[i][j] == 0:
            area += 1
            continue
        if arr[i][j] != 6:
            cctv.append((arr[i][j], i, j))

# 각 cctv에서 방향별 감시 영역 좌표 구하기
# monitored_area[cctv 인덱스] = [방향별 감시 영역]
monitored_area = [monitor(*c) for c in cctv]
monitored_cnt = 0
count_monitored_area(0, len(cctv), set())
print(area - monitored_cnt)
