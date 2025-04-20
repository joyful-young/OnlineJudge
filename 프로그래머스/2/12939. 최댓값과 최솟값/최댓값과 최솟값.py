def solution(s):
    numbers = list(map(int, s.split()))
    max_n = max(numbers)
    min_n = min(numbers)
    return f"{min_n} {max_n}"