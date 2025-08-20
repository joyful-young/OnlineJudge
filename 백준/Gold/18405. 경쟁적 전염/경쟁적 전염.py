import sys
from heapq import heappush, heappop
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, K = map(int, input().split())

virus = []
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(N):
        if arr[i][j] != 0:
            heappush(virus, (arr[i][j], i, j))

S, X, Y = map(int, input().split())

for _ in range(S):
    nxt_virus = []
    while virus:    
        v_type, x, y = heappop(virus)
    
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
    
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = v_type
                heappush(nxt_virus, (v_type, nx, ny))
    virus = nxt_virus

print(arr[X - 1][Y - 1])