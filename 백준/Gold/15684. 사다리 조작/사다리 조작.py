N, M, H = map(int, input().split())

arr = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
    arr[a - 1][b] = 2


def check():
    same = 0
    for i in range(N):
        now = i
        for r in range(H):
            if arr[r][now] == 1:
                now += 1
            elif arr[r][now] == 2:
                now -= 1
        if now == i:
            same += 1
    return same


def dfs(n):
    global answer

    if answer != -1:
        return
    
    temp = check()
    if temp + (cnt - n) * 2 < N:
        return

    if n == cnt:
        if temp == N:
            answer = cnt
        return
    
    for r in range(H):
        for c in range(N-1):
            if arr[r][c] or arr[r][c + 1]:
                continue
            arr[r][c], arr[r][c + 1] = 1, 2
            dfs(n + 1)
            arr[r][c], arr[r][c + 1] = 0, 0


answer = -1
for cnt in range(4):
    dfs(0)
    if answer != -1:
        break

print(answer)