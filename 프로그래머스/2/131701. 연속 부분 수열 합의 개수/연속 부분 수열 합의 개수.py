from collections import deque

def solution(elements):
    sum_set = set(elements + [sum(elements)])
    
    dq = deque(elements)
    N = len(elements)
    for _ in range(N):
        for l in range(2, N):
            sum_set.add(sum(list(dq)[:l]))
        dq.rotate()
    
    return len(sum_set)