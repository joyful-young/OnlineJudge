def solution(x, n):
    if x > 0:
        return [num for num in range(x, x*n + 1, x)]
    elif x == 0:
        return [0] * n
    else:
        return [num for num in range(x, x*n - 1, x)]