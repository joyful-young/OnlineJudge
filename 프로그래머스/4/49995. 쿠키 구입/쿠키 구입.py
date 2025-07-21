def solution(cookie):
    N = len(cookie)
    if N == 1:
        return 0
    
    answer = 0
    for m in range(N - 1):
        l = m
        r = m + 1
        left = cookie[l]
        right = cookie[r]
        
        while True:
            if left == right:
                answer = max(left, answer)
            
            if l > 0 and (left <= right or r == N - 1):
                l -= 1
                left += cookie[l]
            elif r < N - 1:
                r += 1
                right += cookie[r]
            else:
                break
                
    return answer