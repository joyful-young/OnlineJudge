def solution(n):
    sqrt_n = n ** 0.5
    cnt = 0
    for i in range(1, int(sqrt_n) + 1):
        if n % i == 0:
            cnt += 1
    if sqrt_n == int(sqrt_n):
        return 2 * cnt - 1
    return 2 * cnt