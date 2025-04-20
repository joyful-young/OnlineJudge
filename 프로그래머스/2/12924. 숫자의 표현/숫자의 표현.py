def solution(n):
    numbers = [i for i in range(1, n + 1)]
    left = 0
    right = 0
    cur = 0
    cnt = 0
    while left < n:
        
        while cur < n and right < n:
            cur += numbers[right]
            right += 1
            
        if cur == n:
            cnt += 1

        cur -= numbers[left]
        left += 1
            
    return cnt