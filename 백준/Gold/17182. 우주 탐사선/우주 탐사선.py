import sys
input = sys.stdin.readline


N, K = map(int, input().split())
planets = [list(map(int, input().split())) for _ in range(N)]

# 각 행성 간 최소 거리 구하기
dists = [[planets[i][j] for j in range(N)] for i in range(N)]
for k in range(N):
    for s in range(N):
        for e in range(N):
            dists[s][e] = min(dists[s][e], dists[s][k] + dists[k][e])


min_time = 10000
visited = [False for _ in range(N)]


def explore(now, cnt, time):
    global min_time
    if time >= min_time:
        return
        
    if cnt == N:
        min_time = time
        return

    for nxt in range(N):
        if not visited[nxt]:
            visited[nxt] = True
            explore(nxt, cnt + 1, time + dists[now][nxt])
            visited[nxt] = False


visited[K] = True
explore(K, 1, 0)
print(min_time)