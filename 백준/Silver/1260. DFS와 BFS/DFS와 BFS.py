# 재귀
def dfs(v, visited):
    visited[v] = 1
    print(v, end=' ')
    for w in adjL[v]:
        if not visited[w]:
            dfs(w, visited)


def bfs(v, visited):
    # 시작점 인큐
    queue = [v]
    visited[v] = 1

    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        # 현재 정점에 인접한 정점 중 방문하지 않았던 곳 방문
        for w in adjL[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = 1
        # 인접한 곳 다 방문했으면 처음으로 돌아가서 큐에서 정점 꺼내기


N, M, V = map(int, input().split())     # 정점 개수, 간선 개수, 탐색 시작 정점
adjL = [[] for _ in range(N + 1)]   # 정점 번호 1 ~ N
for _ in range(M):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

for i in range(N + 1):
    adjL[i].sort()


visited = [0 for _ in range(N + 1)]
dfs(V, visited)
print()
visited = [0 for _ in range(N + 1)]
bfs(V, visited)
