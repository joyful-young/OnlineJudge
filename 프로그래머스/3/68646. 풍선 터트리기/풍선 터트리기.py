MAX = 1000000000

def solution(a):
    n = len(a)
    left_min = [MAX for _ in range(n)]
    right_min = [MAX for _ in range(n)]
    
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i - 1])
    
    for i in range(n - 1, 0, -1):
        right_min[i - 1] = min(right_min[i], a[i])
        
    answer = n
    for i in range(n):
        if left_min[i] < a[i] and right_min[i] < a[i]:
            answer -= 1
    
    return answer