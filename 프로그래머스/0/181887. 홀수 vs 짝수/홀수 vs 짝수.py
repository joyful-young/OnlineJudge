def solution(num_list):
    n = len(num_list)
    odds = [num_list[idx] for idx in range(n) if idx % 2 == 0]
    evens = [num_list[idx] for idx in range(n) if idx % 2 == 1]
    return max(sum(odds), sum(evens))