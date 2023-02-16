N = int(input())


def stone(a, b, N): # a는상근, b는 창영, N은 돌의수
    if N == 1:
        return a
    elif N == 2 :
        return b
    elif N == 3 :
        return a
    elif N >= 4:
        if N % 4 == 0:
            return b
        if N % 4 == 1:
            return a
        if N % 4 == 2:
            return b
        if N % 4 == 3:
            return a

print(stone('SK','CY',N))