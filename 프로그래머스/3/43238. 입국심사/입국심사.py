def solution(n, times):
    def is_possible(value):
        p = 0
        for time in times:
            p += value // time
        if p >= n:
            return True
        return False
    
    
    # 전체 소요 시간이 될 수 있는 범위
    work_per_min = 0
    min_time = 1000000000
    for time in times:
        work_per_min += 1 / time
        min_time = min(min_time, time)
    left = n // work_per_min
    right = n * min_time
    
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    return answer