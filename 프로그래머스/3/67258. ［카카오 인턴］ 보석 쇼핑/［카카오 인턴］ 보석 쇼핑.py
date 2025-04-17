def solution(gems):
    N = len(gems)
    
    # 보석 종류 수
    T = len(set(gems))
    gem_dict = {}
    
    left = 0
    right = 0
    shortest_interval = [0, 0]
    shortest_length = N + 1
    while left < N:
        
        while len(gem_dict) < T and right < N:
            if gems[right] in gem_dict:
                gem_dict[gems[right]] += 1
            else:
                gem_dict[gems[right]] = 1
            right += 1
        
        if len(gem_dict) == T and right - left < shortest_length:
            shortest_length = right - left
            shortest_interval = [left + 1, right]
            
            
        if gem_dict[gems[left]] == 1:
            del gem_dict[gems[left]]
        else:
            gem_dict[gems[left]] -= 1
        left += 1
        
    return shortest_interval