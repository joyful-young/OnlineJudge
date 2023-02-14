# 백준 7576. 토마토

from collections import deque

di = [0, 1, 0, -1]      # 우하좌상
dj = [1, 0, -1, 0]

M, N = map(int, input().split())    # 열, 행

# 둘레에 -1. 원본 데이터 인덱스는 행: 1 ~ N, 열: 1 ~ M
tomato = [[-1] * (M + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (M + 2)]
# print(tomato)

queue1 = deque()
queue2 = deque()
visited = [[False] * (M + 2) for _ in range(N + 2)]
days = 0

cnt = 0     # 토마토 총 개수 - 다 익었는지 비교용
cnt_ripe = 0        # 익은 토마토 개수

# 익은 토마토 찾기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if tomato[i][j] == 0:       # 안 익은 토마토
            cnt += 1
        elif tomato[i][j] == 1:     # 익은 토마토
            cnt += 1
            cnt_ripe += 1
            tmp = (i, j)
            queue1.append(tmp)

# # 익은 토마토가 없으면 -1 출력
# if not queue1:
#     print(-1)

while queue1 or queue2:     # 큐1이나 큐2가 차 있으면
    while queue1:       # 큐1이 빌 때까지
        i, j = queue1.popleft()
        visited[i][j] = True        # 방문 표시

        for k in range(4):
            i2, j2 = i + di[k], j + dj[k]
            if not visited[i2][j2] and tomato[i2][j2] == 0:
                next_node = (i2, j2)
                visited[i2][j2] = True
                queue2.append(next_node)        # 다른 큐에 익은 토마토 넣기
                cnt_ripe += 1
    else:       # 큐1이 비면 날짜 증가시키는데,
        if queue2:      # 큐2 비우고 난 상태에서 큐1이 비어있을 경우에도 증가시키면 안 됨
            days += 1
    # days += 1
    # print('days', days)

    while queue2:       # 큐2가 빌 때까지
        i, j = queue2.popleft()
        visited[i][j] = True

        for k in range(4):
            i2, j2 = i + di[k], j + dj[k]
            if not visited[i2][j2] and tomato[i2][j2] == 0:
                next_node = (i2, j2)
                visited[i2][j2] = True
                queue1.append(next_node)
                cnt_ripe += 1
    else:           # 큐2를 비우면 날짜 증가시키는데,
        if queue1:      # 큐1 비우고 난 상태에서 큐2가 비어있을 경우에도 증가시키면 안 됨
            days += 1
    # days += 1

# print(cnt, cnt_ripe)
# 반복이 끝났을 때
if cnt == cnt_ripe:
    print(days)
else:
    print(-1)


