# 백준 2606. 바이러스

computers = int(input())
link = int(input())

# 컴퓨터 간 연결 관계를 나타내는 리스트
graph = [[] for _ in range(computers + 1)]

for i in range(link):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 방문 여부
visited = [False] * (computers + 1)     # 0번 컴퓨터까지

# 감염된 컴퓨터
cnt = 0


# dfs
def dfs(node, graph, visited):
    visited[node] = True
    global cnt
    cnt += 1
    for i in graph[node]:   # node와 연결된 컴퓨터들에 대해
        if not visited[i]:  # 방문한 적이 없으면
            dfs(i, graph, visited)


dfs(1, graph, visited)

# 1번 컴퓨터 제외
print(cnt - 1)
