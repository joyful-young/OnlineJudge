import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
max_height = 0
min_height = 100
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(N):
        if arr[i][j] < min_height:
            min_height = arr[i][j]
        if arr[i][j] > max_height:
            max_height = arr[i][j]


def count_area(height):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1 or arr[i][j] <= height:
                continue
                
            cnt += 1
            stack = [(i, j)]
            while stack:
                xi, xj = stack.pop()
                if visited[xi][xj] == 1:
                    continue

                visited[xi][xj] = 1
                for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ni, nj = xi + di, xj + dj
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] > height:
                        stack.append((ni, nj))
    return cnt

max_cnt = 1
for h in range(min_height, max_height):    # max_height로 확인하면 어차피 0
    max_cnt = max(max_cnt, count_area(h))
print(max_cnt)