# 백준 2606. 바이러스
# 재귀 말고 스택이랑 반복으로 풀어보기

computers = int(input())
link = int(input())

# 컴퓨터 간 연결 관계를 나타내는 리스트
graph = [[] for _ in range(computers + 1)]

for i in range(link):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 현재 방문 중인 노드를 넣을 스택
stack = [1]

visited = [False] * (computers + 1)     # 방문 여부
visited[1] = True

# 1번부터 시작해 방문하는 노드 수
cnt = 0

# 스택이 비지 않았으면 계속
while stack:
    node = stack.pop()
    # 현재 노드에 연결된 노드들에 대해 반복
    for next_node in graph[node]:
        # 방문한 적 없는 곳이면
        if not visited[next_node]:
            # 방문
            visited[next_node] = True
            # 방문 횟수 추가
            cnt += 1
            # 그 노드로 이동
            stack.append(next_node)

print(cnt)
