from collections import deque

N = int(input())
scv = list(map(int, input().split())) + [0] * (3 - N)
scv.sort(reverse=True)
scv = tuple(scv)

damages = [
    (-9, -3, -1), (-9, -1, -3), 
    (-3, -9, -1), (-3, -1, -9), 
    (-1, -9, -3), (-1, -3, -9)
]
visited = {}
def bfs():
    q = deque([scv])
    visited[scv] = 0
    while q:
        now_scv = q.popleft()
        if now_scv == (0, 0, 0):
            return visited[(0, 0, 0)]

        for damage in damages:
            nxt_scv = tuple(sorted([max(now_scv[i] + damage[i], 0) for i in range(3)], reverse=True))
            
            if not nxt_scv in visited:
                visited[nxt_scv] = visited[now_scv] + 1
                q.append(nxt_scv)

print(bfs())