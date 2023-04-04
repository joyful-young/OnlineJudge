# 백준 9663. N-Queen
def f(i, k):
    global cnt
    if i == k:
        cnt += 1
        return
    for j in range(k):
        if col[j] == 0 and d1[i + j] == 0 and d2[i + (N - 1 - j)] == 0:     # 놓을 수 있으면
            arr[i][j] = 1       # 퀸 놓고
            col[j] = 1
            d1[i + j] = 1
            d2[i + (N - 1 - j)] = 1     # 표시하고
            f(i + 1, k)         # 다음 행에 놓으러 감
            arr[i][j] = 0       # 돌아오면 지우기
            col[j] = 0
            d1[i + j] = 0
            d2[i + (N - 1 - j)] = 0


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
# row = [0] * N
col = [0] * N
d1 = [0] * (2 * N - 1)      # / 대각선. i + j
d2 = [0] * (2 * N - 1)      # \ 대각선. i + (N - 1 - j)
cnt = 0
f(0, N)     # N개의 퀸 놓기
print(cnt)