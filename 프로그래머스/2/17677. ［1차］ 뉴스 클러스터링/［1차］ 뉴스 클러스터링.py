from collections import defaultdict

N = 65536


def solution(str1, str2):
    set1 = get_str_set(str1)
    set2 = get_str_set(str2)
    
    intersection_dict = dict()
    union_dict = {k: v for k, v in set2.items()}
    
    for s in set1:
        if s in set2:
            intersection_dict[s] = min(set1[s], set2[s])
            union_dict[s] = max(set1[s], set2[s])
        else:
            union_dict[s] = set1[s]
    
    numer = sum(intersection_dict.values())
    denom = sum(union_dict.values())
    if denom == 0:
        return N
    return int(N * numer / denom)


def get_str_set(s):
    str_set = defaultdict(int)
    for i in range(len(s) - 1):
        if s[i:i + 2].isalpha():
            str_set[s[i:i + 2].lower()] += 1
    return str_set