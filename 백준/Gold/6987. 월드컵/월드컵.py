import sys
input = sys.stdin.readline

# 6개국, 총 15경기
T = 6
matches = [(i, j) for i in range(T - 1) for j in range(i + 1, T)]
M = len(matches)


def bt(x, win, draw, lose):
    if x == M:
        return True

    a, b = matches[x]

    # a 승
    if win[a] > 0 and lose[b] > 0:
        win[a] -= 1
        lose[b] -= 1
        
        if bt(x + 1, win, draw, lose):
            return True
        
        win[a] += 1
        lose[b] += 1

    # a 패
    if lose[a] > 0 and win[b] > 0:
        lose[a] -= 1
        win[b] -= 1

        if bt(x + 1, win, draw, lose):
            return True

        lose[a] += 1
        win[b] += 1

    # 무승부
    if draw[a] > 0 and draw[b] > 0:
        draw[a] -= 1
        draw[b] -= 1

        if bt(x + 1, win, draw, lose):
            return True
            
        draw[a] += 1
        draw[b] += 1

    return False


def is_possible(arr):
    """
    6 x 3 배열
    """
    # 각 행의 합이 5인지 확인
    for row in arr:
        if sum(row) != 5:
            return False

    # 승무패
    win, draw, lose = list(map(list, zip(*arr)))

    sw, sd, sl = sum(win), sum(draw), sum(lose)
    if sw != sl:
        return False

    if sw + sd + sl != 30:
        return False

    if sd % 2:
        return False

    return bt(0, win, draw, lose)

res = [0] * 4
for i in range(4):
    tmp = list(map(int, input().split()))
    if is_possible([tmp[i:i+3] for i in range(0, 18, 3)]):
        res[i] = 1
print(*res)
