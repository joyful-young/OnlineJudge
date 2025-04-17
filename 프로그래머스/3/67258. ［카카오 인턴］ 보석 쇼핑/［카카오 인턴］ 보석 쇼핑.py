def solution(gems):
    N = len(gems)
    
    # 보석 종류 수
    T = len(set(gems))
    gem_dict = {}
    
    left = 0
    right = 0
    interval = [1, N]
    while left < N:
        
        while len(gem_dict) < T and right < N:
            if gems[right] in gem_dict:
                gem_dict[gems[right]] += 1
            else:
                gem_dict[gems[right]] = 1
            right += 1
        
        if len(gem_dict) == T and right - left < interval[1] - interval[0] + 1:
            interval = [left + 1, right]
            
            
        if gem_dict[gems[left]] == 1:
            del gem_dict[gems[left]]
        else:
            gem_dict[gems[left]] -= 1
        left += 1
        
    return interval