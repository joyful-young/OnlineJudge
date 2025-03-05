N, M = map(int, input().split())
arr = [[False for _ in range(M)] for _ in range(N)]
cnt = 0


def dfs(l, c):
    global cnt
    if l == N:
        cnt += 1
        return
    
    # 다음 칸 구하기
    nxt_l, nxt_c = (l, c + 1) if c + 1 < M else (l + 1, 0)

    # (l, c)에 넴모 안 둘 경우
    dfs(nxt_l, nxt_c)

    # (l, c)에 넴모 둘 경우
    # (l - 1, c - 1), (l - 1, c), (l, c - 1) 위치가 모두 True이면 (l, c)에는 True 불가
    if l >= 1 and c >= 1 and arr[l - 1][c - 1] and arr[l - 1][c] and arr[l][c - 1]:
        return

    arr[l][c] = True
    dfs(nxt_l, nxt_c)
    arr[l][c] = False
    

dfs(0, 0)
print(cnt)