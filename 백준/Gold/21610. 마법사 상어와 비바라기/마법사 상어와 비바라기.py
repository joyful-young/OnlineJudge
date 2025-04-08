import sys
input = sys.stdin.readline

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

def move(d, s, cloud):
    # 1. 모든 구름이 d 방향으로 s칸 이동
    # 2. 구름에서 비 내려 각 칸 물의 양 1 증가
    moved = set()
    for r, c in cloud:
        nr = (r + s * di[d]) % N
        nc = (c + s * dj[d]) % N
        moved.add((nr, nc))
        arr[nr][nc] += 1

    # 3. 4. 대각선 방향 물 복사
    water_add = []
    for r, c in moved:
        count = 0
        for k in range(1, 8, 2):
            nr, nc = r + di[k], c + dj[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > 0:
                count += 1
        water_add.append((r, c, count))

    for r, c, cnt in water_add:
        arr[r][c] += cnt

    # 5. 새로운 구름 생성
    new_cloud = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in moved:
                new_cloud.add((i, j))
                arr[i][j] -= 2

    return new_cloud

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = set([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])

for _ in range(M):
    direction, dist = map(int, input().split())
    cloud = move(direction - 1, dist, cloud)

print(sum(map(sum, arr)))
