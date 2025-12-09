import sys
input = sys.stdin.readline


N, M, H = map(int, input().split())
arr = [[False] * N for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = True


def go_down(n, ladder):
    for r in range(1, H + 1):
        if n < N and ladder[r][n]:
            n += 1
        elif n > 1 and ladder[r][n - 1]:
            n -= 1
    return n


def is_valid(ladder):
    for i in range(1, N + 1):
        if i != go_down(i, ladder):
            return False
    return True


# 3 초과하면 -1 출력
answer = 4
candidates = []
for r in range(1, H + 1):
    for c in range(1, N):
        if arr[r][c]:
            continue
        if c < N - 1 and arr[r][c + 1]:
            continue
        if c > 1 and arr[r][c - 1]:
            continue

        candidates.append((r, c))



def bt(start_idx, cnt):
    global answer

    if cnt >= answer:
        return

    if is_valid(arr):
        answer = cnt
        return

    if cnt == 3:
        return

    for idx in range(start_idx, len(candidates)):
        r, c = candidates[idx]

        if arr[r][c]:
            continue
            
        # 왼쪽에 이미 있는 경우
        if c > 1 and arr[r][c - 1]:
            continue

        if c < N - 1 and arr[r][c + 1]:
            continue

        arr[r][c] = True
        bt(idx + 1, cnt + 1)
        arr[r][c] = False


bt(0, 0)
print(answer if answer <= 3 else -1)