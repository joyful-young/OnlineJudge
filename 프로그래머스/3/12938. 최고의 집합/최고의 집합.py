def solution(n, s):
    if n > s:
        return [-1]
    q, r = divmod(s, n)
    return [q] * (n - r) + [q + 1] * r