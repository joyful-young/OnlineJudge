def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        # 바위 사이 최소 거리가 mid가 되기 위해 제거해야 할 바위의 최소 개수
        if remove_rocks(distance, rocks, mid) <= n:
            answer = max(mid, answer)
            left = mid + 1
        else:
            right = mid - 1
        
    return answer


def remove_rocks(distance, rocks, min_d):
    # 최소 거리가 mid_d가 되도록 간격이 min_d보다 작으면 바위 제거
    s = 0
    cnt = 0
    for e in rocks:
        if e - s < min_d:
            cnt += 1
        else:
            s = e
    if distance - s < min_d:
        cnt += 1
    return cnt