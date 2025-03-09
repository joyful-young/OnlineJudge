def solution(my_string, indices):
    idx_set = set(indices)
    answer = [my_string[idx] for idx in range(len(my_string)) if idx not in idx_set]
    return ''.join(answer)