import sys
from collections import deque
input = sys.stdin.readline

directions = [(0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0)]
M, N, H = map(int, input().split())
boxes = [[0 for _ in range(N)] for _ in range(H)]
visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
tomatoes = deque()
cnt = M * N * H
for h in range(H):
    for r in range(N):
        boxes[h][r] = list(map(int, input().split()))
        for c in range(M):
            if boxes[h][r][c] == 1:
                tomatoes.append((h, r, c))
                visited[h][r][c] = 0
                cnt -= 1
            elif boxes[h][r][c] == -1:
                cnt -= 1

def bfs(cnt):
    if cnt == 0:
        return 0
        
    while tomatoes:
        xh, xn, xm = tomatoes.popleft()
    
        for dh, dn, dm in directions:
            nh, nn, nm = xh + dh, xn + dn, xm + dm
            if not (0 <= nh < H and 0 <= nn < N and 0 <= nm < M):
                continue
    
            if boxes[nh][nn][nm] == 0 and visited[nh][nn][nm] == -1:
                cnt -= 1
                visited[nh][nn][nm] = visited[xh][xn][xm] + 1
                if cnt == 0:
                    return visited[nh][nn][nm]
                    
                tomatoes.append((nh, nn, nm))
                
    return -1

print(bfs(cnt))