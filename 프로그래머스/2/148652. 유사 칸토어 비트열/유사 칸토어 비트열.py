FIRST = "11011"

def solution(n, l, r):
    return count_one(n, l - 1, r - 1)


def count_one(n, left, right):  # left, right은 0-base idx
    if n == 1:
        return FIRST[left:right + 1].count("1")
    
    five_pow = 5 ** (n - 1)
    lq, lr = divmod(left, five_pow)
    rq, rr = divmod(right, five_pow)
    
    if lq == rq:
        if lq == 2:
            return 0
        return count_one(n - 1, lr, rr)
    
    if lq == 2:
        answer = count_one(n - 1, 0, rr)
    elif rq == 2:
        answer = count_one(n - 1, lr, five_pow - 1)
    else:
        answer = count_one(n - 1, lr, five_pow - 1) + count_one(n - 1, 0, rr)

    for i in range(lq + 1, rq):
        if i != 2:
            answer += count_one(n - 1, 0, five_pow - 1)
    return answer
