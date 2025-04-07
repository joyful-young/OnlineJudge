import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

def bfs(start, goal):
    q = deque([start])
    visited = [-1 for _ in range(100001)]
    visited[start] = 0

    while q:
        v = q.popleft()

        if v == goal:
            return visited[v]

        for w in [v - 1, v + 1, 2*v]:
            if 0 <= w <= 100000 and visited[w] == -1:
                visited[w] = visited[v] + 1
                q.append(w)

print(bfs(N, K))