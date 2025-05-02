def solution(diffs, times, limit):
    n = len(diffs)
    left = 1
    right = 100000
    answer = 100000
    while left <= right:
        mid = (left + right) // 2
        
        total_time = times[0]
        for i in range(1, n):
            total_time += calc_time(diffs[i], times[i], times[i - 1], mid)
            if total_time > limit:
                left = mid + 1
                break
        else:
            answer = min(answer, mid)
            right = mid - 1
    
    return answer


def calc_time(diff, time_cur, time_prev, level):
    if diff <= level:
        return time_cur
    
    return (diff - level) * (time_cur + time_prev) + time_cur