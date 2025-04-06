import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    v, w = map(int, input().split())
    adjL[v].append(w)
    adjL[w].append(v)


def dfs(start):
    result = []
    stack = [start]
    visited = [0 for _ in range(N + 1)]

    while stack:
        v = stack.pop()
        if visited[v]:
            continue

        visited[v] = 1
        result.append(v)
        for w in sorted(adjL[v], reverse=True):    # 번호 큰 것부터 스택에 넣기
            if not visited[w]:
                stack.append(w)
                
    return result


def bfs(start):
    result = []
    q = deque([start])
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1

    while q:
        v = q.popleft()
        result.append(v)

        for w in sorted(adjL[v]):
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                
    return result

print(*dfs(V))
print(*bfs(V))