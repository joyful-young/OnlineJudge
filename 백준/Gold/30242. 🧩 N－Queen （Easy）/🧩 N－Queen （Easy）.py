N = int(input())
queens = list(map(int, input().split()))

col_used = set()
rc_diff = set()    # (row - col)
rc_sum = set()     # (row + col)
for row in range(N):
    if queens[row] != 0:
        col = queens[row] - 1
        col_used.add(col)
        rc_diff.add(row - col)
        rc_sum.add(row + col)
        

def backtrack(row):
    global ans_flag
    if ans_flag:
        return

    if row == N:
        ans_flag = True
        print(*queens)
        return

    # 이미 퀸이 그 행에 배치된 경우 다음 행으로
    if queens[row] != 0:
        backtrack(row + 1)
        return

    for col in range(N):
        # 배치 불가능한 경우
        if col in col_used or (row - col) in rc_diff or (row + col) in rc_sum:
            continue

        # 배치
        queens[row] = col + 1
        col_used.add(col)
        rc_diff.add(row - col)
        rc_sum.add(row + col)

        backtrack(row + 1)

        queens[row] = 0
        col_used.remove(col)
        rc_diff.remove(row - col)
        rc_sum.remove(row + col)

ans_flag = False
backtrack(0)
if not ans_flag:
    print(-1)
