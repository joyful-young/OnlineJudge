def solution(stones, k):
    def is_possible(m):
        cnt = 0    # m명의 사람이 건널 수 없는 연속되는 돌 개수
        for stone in stones:
            if stone - m < 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == k:
                return False
        return True
    
    left = 0
    right = 200000000
    ans = right
    while left <= right:
        # 건널 수 있는 사람 수
        mid = (left + right) // 2
        if is_possible(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
        
    return ans