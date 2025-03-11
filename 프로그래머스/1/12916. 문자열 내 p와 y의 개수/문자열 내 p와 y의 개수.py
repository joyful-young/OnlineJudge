def solution(s):
    p, y = 0, 0
    for c in s.lower():
        if c == "p":
            p += 1
        elif c == "y":
            y += 1

    return p == y