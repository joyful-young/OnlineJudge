# 무기공학
import sys
input = sys.stdin.readline

WINGS = [(-1, 0, 0, 1), (0, 1, 1, 0), (1, 0, 0, -1), (0, -1, -1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_strength = 0
visited = [[False] * M for _ in range(N)]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M and not visited[r][c]


def bt(r, c, cur_sum):
    global max_strength
    
    if r == N:
        max_strength = max(max_strength, cur_sum)
        return
    
    if c == M - 1:
        nr = r + 1
        nc = 0
    else:
        nr = r
        nc = c + 1
    
    if visited[r][c]:
        bt(nr, nc, cur_sum)
        return
    
    for dr1, dc1, dr2, dc2 in WINGS:
        wr1 = r + dr1
        wc1 = c + dc1
        wr2 = r + dr2
        wc2 = c + dc2
        
        if is_valid(wr1, wc1) and is_valid(wr2, wc2):
            visited[wr1][wc1] = True
            visited[wr2][wc2] = True
            visited[r][c] = True
            
            bt(nr, nc, cur_sum + arr[wr1][wc1] + arr[wr2][wc2] + 2 * arr[r][c])
            
            visited[wr1][wc1] = False
            visited[wr2][wc2] = False
            visited[r][c] = False
    
    bt(nr, nc, cur_sum)
    

bt(0, 0, 0)
print(max_strength)