# 백준 2644. 촌수계산

from collections import deque


def bfs(s, g):
    queue = deque([s])
    visited = [False] * (n + 1)     # 방문여부 표시
    distance = [-1] * (n + 1)       # 촌수 표시 리스트 초기화
    distance[s] = 0                 # 출발지점 거리 0

    while queue:    # 큐가 빌 때까지
        node = queue.popleft()     # 큐에 먼저 들어갔던 게 현재 노드
        visited[node] = True        # 방문 노드 표시

        if node == g:               # 방문한 곳이 목표지점이면
            return distance[g]

        for next_node in graph[node]:       # 노드와 인접한 노드 중
            if not visited[next_node]:      # 방문 안 한 곳이 있으면
                visited[next_node] = True   # 방문
                queue.append(next_node)     # 노드 큐에 넣기
                distance[next_node] = distance[node] + 1    # 이전 노드의 출발지점에서의 거리에 +1
    # 목표 지점 방문하지 못하고 끝나면
    return distance[g]      # 초기화를 -1로 해서 -1 나올 것


n = int(input())

person1, person2 = map(int, input().split())

graph = [[] for _ in range(n + 1)]

m = int(input())

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(person1, person2))
