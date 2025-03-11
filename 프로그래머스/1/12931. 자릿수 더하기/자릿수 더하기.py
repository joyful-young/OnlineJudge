def solution(n):
    answer = 0
    while n > 0:
        n, r = divmod(n, 10)
        answer += r
    return answer