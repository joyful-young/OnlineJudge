import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

def bfs():
    q = deque([S])
    visited = [-1 for _ in range(F + 1)]
    visited[S] = 0

    while q:
        v = q.popleft()

        if v == G:
            return visited[G]

        for w in [v + U, v - D]:
            if 1 <= w <= F and visited[w] == -1:
                visited[w] = visited[v] + 1
                q.append(w)
                
    return "use the stairs"

print(bfs())