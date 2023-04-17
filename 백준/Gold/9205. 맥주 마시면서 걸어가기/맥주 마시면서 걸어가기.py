# 백준 9205. 맥주 마시면서 걸어가기

from collections import deque


def bfs():
    q = deque()
    visited = [0 for _ in range(n + 2)]
    q.append(arr[0])
    visited[0] = 1

    while q:
        ti, tj = q.popleft()
        if [ti, tj] == arr[n + 1]:
            print('happy')
            break
        for i in range(1, n + 2):
            if not visited[i] and abs(arr[i][0] - ti) + abs(arr[i][1] - tj) <= 1000:
                q.append(arr[i])
                visited[i] = 1

    if not visited[n + 1]:
        print('sad')


t = int(input())
for _ in range(t):
    n = int(input())    # 편의점의 개수

    arr = [list(map(int, input().split())) for _ in range(n + 2)]

    bfs()
