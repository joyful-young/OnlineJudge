N, M = map(int, input().split())
arr = [[False for _ in range(M)] for _ in range(N)]
cnt = 0


def dfs(row, col):
    global cnt
    if row == N:
        cnt += 1
        return
    
    # 다음 칸 구하기
    nxt_row, nxt_col = (row, col + 1) if col + 1 < M else (row + 1, 0)

    # (row, col)에 넴모 안 둘 경우
    dfs(nxt_row, nxt_col)

    # (row, col)에 넴모 둘 경우
    # (row - 1, col - 1), (row - 1, col), (row, col - 1) 위치가 모두 True이면 (row, col)에는 True 불가
    if row >= 1 and col >= 1 and arr[row - 1][col - 1] and arr[row - 1][col] and arr[row][col - 1]:
        return

    arr[row][col] = True
    dfs(nxt_row, nxt_col)
    arr[row][col] = False
    

dfs(0, 0)
print(cnt)