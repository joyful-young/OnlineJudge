from collections import defaultdict

def solution(k, tangerine):
    size_dict = defaultdict(int)
    for t in tangerine:
        size_dict[t] += 1
    
    tangerine_sizes = sorted(list(size_dict.values()), reverse=True)
    answer = 0
    while k > 0:
        k -= tangerine_sizes[answer]
        answer += 1
    return answer