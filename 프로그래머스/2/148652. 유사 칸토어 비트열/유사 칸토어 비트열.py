def solution(n, l, r):
    answer = r - l + 1
    for idx in range(l - 1, r):     # 0-base idx
        while idx > 0:
            idx, r = divmod(idx, 5)
            
            if r == 2 or idx == 2:      # 00000 구간 or 11011 에서 0
                answer -= 1
                break

    return answer