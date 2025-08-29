import sys
input = sys.stdin.readline


N = int(input())
fruits = list(map(int, input().split()))
adjL = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)


def dfs(start):
    max_fruits = fruits[start - 1]
    farthest_node = start
    
    stack = [(start, max_fruits)]
    dist = [-1] * (N + 1)
    dist[start] = max_fruits

    while stack:
        v, f = stack.pop()

        if f > max_fruits:
            max_fruits = f
            farthest_node = v

        for w in adjL[v]:
            if dist[w] == -1:
                dist[w] = f + fruits[w - 1]
                stack.append([w, dist[w]])
    return farthest_node, max_fruits, dist


# 임의의 노드(1번)에서 시작해 열매가 최대가 되는 다른 끝 노드
end1 = dfs(1)[0]

# end1에서 시작해 열매가 최대가 되도록 하는 다른 끝 노드
end2, max_fruits, dist1 = dfs(end1)

_, _, dist2 = dfs(end2)

best_start = None
for i in range(1, N + 1):
    if max(dist1[i], dist2[i]) == max_fruits:
        if best_start is None or i < best_start:
            best_start = i

print(max_fruits, best_start)