def solution(topping):
    N = len(topping)
    if N <= 1:
        return 0
    
    right = {}
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1
    
    
    left = {}
    answer = 0
    for i in range(N - 1):    # 인덱스 0 ~ i / (i + 1) ~ (N - 1)로 나누기
        if topping[i] in left:
            left[topping[i]] += 1
        else:
            left[topping[i]] = 1
        
        if right[topping[i]] == 1:
            del right[topping[i]]
        else:
            right[topping[i]] -= 1
        
        if len(left) == len(right):
            answer += 1
    
    return answer