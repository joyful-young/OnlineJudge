# 1167. 트리의 지름
import sys
input = sys.stdin.readline

V = int(input())
adjL = [[] for _ in range(V + 1)]

for _ in range(1, V + 1):
    edge_info = list(map(int, input().split()))
    node = edge_info[0]
    for i in range(1, len(edge_info) - 1, 2):
        adjL[node].append([edge_info[i], edge_info[i + 1]])    # [인접 노드, 거리]


def dfs(start):
    visited = [0 for _ in range(V + 1)]
    stack = [[start, 0]]
    visited[start] = 1
    farthest_node, max_dist = start, 0

    while stack:
        v, d = stack.pop()
        if d > max_dist:
            max_dist = d
            farthest_node = v

        for w, v_to_w in adjL[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append([w, d + v_to_w])
    return farthest_node, max_dist


# 임의의 노드에서 가장 먼 노드 A 찾기
farthest = dfs(1)[0]

# A에서 가장 먼 노드까지의 거리 구하기
print(dfs(farthest)[1])