import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
adjL = [[] for _ in range(V + 1)]    # 1번 ~ V번
for _ in range(E):
    v, w = map(int, input().split())
    adjL[v].append(w)
    adjL[w].append(v)

def dfs(start):
    stack = [start]
    visited = [0 for _ in range(V + 1)]

    while stack:
        v = stack.pop()

        if visited[v] == 1:
            continue

        visited[v] = 1

        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(w)

    return sum(visited) - 1

print(dfs(1))