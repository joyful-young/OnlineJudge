import sys
input = sys.stdin.readline

N = 10
M = 5
arr = [list(map(int, input().split())) for _ in range(N)]

paper_cnt = [0 for _ in range(M + 1)]
MAX_V = 26
min_value = MAX_V

pasted = set()

def can_paste(r, c, l):
    if r + l > N or c + l > N:
        return False
        
    for i in range(r, r + l):
        for j in range(c, c + l):
            if arr[i][j] == 0 or (i, j) in pasted:
                return False
    return True

def set_paste(r, c, l, flag):
    """
    True면 붙이기, False면 떼기
    """
    for i in range(r, r + l):
        for j in range(c, c + l):
            if flag:
                pasted.add((i, j))
            else:
                pasted.remove((i, j))


def paste(r, c, cnt):
    global min_value
    
    if cnt >= min_value:
        return
        
    if r >= N:
        min_value = min(min_value, cnt)
        return
        
    if c >= N:
        paste(r + 1, 0, cnt)
        return

    if arr[r][c] == 1 and (r, c) not in pasted:
        # 아직 안 붙인 1
        for l in range(M, 0, -1):
            if paper_cnt[l] >= 5:
                continue
                
            if can_paste(r, c, l):
                set_paste(r, c, l, True)
                paper_cnt[l] += 1
                paste(r, c + 1, cnt + 1)
                set_paste(r, c, l, False)
                paper_cnt[l] -= 1
    else:
        # 0이거나 이미 붙인 1
        paste(r, c + 1, cnt)

paste(0, 0, 0)
print(min_value if min_value != MAX_V else -1)
