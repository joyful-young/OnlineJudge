from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    for c, t in clothes:
        clothes_dict[t].append(c)
        
    answer = 1
    for v in clothes_dict.values():
        answer *= len(v) + 1
    return answer - 1