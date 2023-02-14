# 백준 2178. 미로 탐색

from collections import deque

di = [0, 1, 0, -1]      # 우하좌상
dj = [1, 0, -1, 0]

N, M = map(int, input().split())

input_arr = [[0] + list(map(int, list(input()))) + [0] for _ in range(N)]

# 인덱스랑 좌표랑 맞추기 + padding
arr = [[0] * (M + 2)] + input_arr + [[0] * (M + 2)]     # (N + 2) x (M + 2)
# print(arr)

start = (1, 1)
goal = (N, M)

queue = deque()
queue.append(start)
visited = [[False] * (M + 2) for _ in range(N + 2)]
# print(visited)
distance = [[0] * (M + 2) for _ in range(N + 2)]

while queue:        # 큐가 빌 때까지
    i, j = queue.popleft()
    node = (i, j)
    visited[i][j] = True    # 방문 표시

    if node == goal:                    # 도착 시 반복문 중단
        break

    for k in range(4):
        i2, j2 = (i + di[k], j + dj[k])
        next_node = (i2, j2)
        if (not visited[i2][j2]) and arr[i2][j2]:         # 상하좌우 중 방문 안 한 곳이 있고 그곳이 1이면
            visited[i2][j2] = True      # 방문
            queue.append(next_node)
            distance[i2][j2] = distance[i][j] + 1

# 출발지 포함 지나간 칸 수는 거리에 +1
print(distance[N][M] + 1)
