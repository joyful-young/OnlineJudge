# 백준 1260. DFS와 BFS

# 정점 번호 작은 것을 먼저 방문

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 작은 숫자가 먼저 나오게 정렬
for i in range(N + 1):
    graph[i].sort()

visited_dfs = [False] * (N + 1)


def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node, visited)


def bfs(v):
    queue = [v]
    visited = [False] * (N + 1)
    visited[v] = True
    print(v, end=' ')

    while queue:
        node = queue.pop(0)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                print(next_node, end=' ')


dfs(V, visited_dfs)
print()
bfs(V)
